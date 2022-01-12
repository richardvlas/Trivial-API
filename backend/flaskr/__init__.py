import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from sqlalchemy.sql.expression import select

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginated_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
  

    # Set up CORS. Allow '*' for origins.
    CORS(app, resources={"/": {"origins": "*"}})
  
    # CORS Headers - Use the after_request decorator to set Access-Control-Allow
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response


    # Create an endpoint to handle GET requests for all available categories.
    @app.route('/categories', methods=['GET'])
    def get_categories():
        data = Category.query.order_by(Category.id).all()        

        categories = {category.id: category.type for category in data}
        
        # If no categories found (404 Not Found)
        if len(categories) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'categories': categories
        })


    ''' 
    Create an endpoint to handle GET requests for questions, 
    including pagination (every 10 questions). 
    This endpoint should return a list of questions, 
    number of total questions, current category, categories. 

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions. 
    '''
    @app.route('/questions', methods=['GET'])
    def get_questions():
        
        # get all questions and paginate
        selection = Question.query.order_by(Question.id).all()
        total_questions = len(selection)
        current_question = paginated_questions(request, selection)
        
        # If no questions found (404 Not Found)
        if len(current_question) == 0:
            abort(404)

        # get all categories
        data = Category.query.order_by(Category.id).all()        
        categories = {category.id: category.type for category in data}

        return jsonify({
            'success': True,
            'questions': current_question,
            'total_questions': total_questions,
            'categories': categories,
        })


    '''
    Create an endpoint to DELETE question using a question ID. 

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page. 
    '''
    @app.route('/questions/<int:id>', methods=['DELETE'])
    def delete_question(id):
        try: 
            question = Question.query.filter(Question.id == id).one_or_none()

            # If no question found (404 Not Found)
            if question is None:
                abort(404)

            # Delete the question
            question.delete()                

            return jsonify({
                'success': True,
                'deleted': id
            })
          
        except:
            # If backend was not able to process (422 Unprocessable Entity)
            abort(422)


    '''
    Create an endpoint to POST a new question, 
    which will require the question and answer text, 
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab, 
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.  
    '''
    @app.route('/questions', methods=['POST'])
    def create_question():
        # Get data from request body 
        data = request.get_json()

        new_question = data.get('question')
        new_answer = data.get('answer')
        new_category = data.get('category')
        new_difficulty = data.get('difficulty')

        try:
            # create and insert a new question
            question = Question(question=new_question, answer=new_answer,
                category=new_category, difficulty=new_difficulty)
            question.insert()

            return jsonify({
                'success': True,
                'created': question.id,
                'total_questions': len(Question.query.all())
            })

        except:
            # If backend was not able to process (422 Unprocessable Entity)
            abort(422)


    '''
    Create a POST endpoint to get questions based on a search term. 
    It should return any questions for whom the search term 
    is a substring of the question. 

    TEST: Search by any phrase. The questions list will update to include 
    only question that include that string within their question. 
    Try using the word "title" to start. 
    '''
    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        # Get data from request body 
        body = request.get_json()
        search = body.get('searchTerm', None)
        
        # query the database with search term string
        selection = Question.query.filter(Question.question.ilike(f"%{search}%")).all()

        # If no search term was added found (404 Not Found)
        if len(selection) == 0:
            abort(404)
        else:
            current_question = paginated_questions(request, selection)

        return jsonify({
            'success': True,
            'questions': current_question,
            'total_questions': len(selection),
            'current_category': None
        })


    '''
    Create a GET endpoint to get questions based on category. 

    TEST: In the "List" tab / main screen, clicking on one of the 
    categories in the left column will cause only questions of that 
    category to be shown. 
    '''
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_category_questions(category_id):
        # Get category by id
        category = Category.query.filter(Category.id==category_id).one_or_none()

        try:
            selection = Question.query.filter(
                Question.category == str(category_id)
            ).all()
            total_questions = len(selection)

            questions = [question.format() for question in selection]

            return jsonify({
              'success': True,
              'questions': questions,
              'total_questions': total_questions,
              'currentCategory': category.type
            })

        except:
            # If no data found (404 Not Found)
            abort(404)


    '''
    Create a POST endpoint to get questions to play the quiz. 
    This endpoint should take category and previous question parameters 
    and return a random questions within the given category, 
    if provided, and that is not one of the previous questions. 

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not. 
    '''
    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        # Get data from request body 
        data = request.get_json()

        try:
            previous_questions = data.get('previous_questions', None)
            quiz_category = data.get('quiz_category', None)
            
            if isinstance(quiz_category, dict):
                # if request body is dict of the form such 
                # as: {"type": "Art", "id": 2} then select only 'id'
                quiz_category = quiz_category['id']

            if quiz_category == 0:
                # if category id is 0, get all questions previously not selected
                # from all categories
                questions = Question.query.all()
            else:
                questions = Question.query.filter(
                    Question.category == quiz_category).all()
            
            questions_not_asked = [question.format() for question in questions 
                if question.id not in previous_questions]
                   
            new_question = random.choice(questions_not_asked)
            
            return jsonify({
                  'success': True,
                  'question': new_question
            })

        except:
            abort(422)


    # Create error handlers for all expected errors including 404 and 422. 
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422


    return app