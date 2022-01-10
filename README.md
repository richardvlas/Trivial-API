# Full Stack Trivia API Project

This project is a demonstration of how to develop and use API and API documentation with the main goal to build a trivia API. Trivia is an game app that allows to:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

By completing this trivia app, various abilities such as to structure plan, implement, and test an API are demonstrated - skills essential for enabling any future applications to communicate with others.

## Getting Started - Backend

### Installing Dependencies
1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the python docs

2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the [`backend`](/backend) directory and running:

```
pip install -r requirements.txt
```

This will install all of the required packages we selected within the [`requirements.txt`](/backend/requirements.txt) file.

4. **Key Dependencies**
- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight PostgreSQL database. You'll primarily find code related to the database in the `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) is the extension we'll use to handle cross origin requests from our frontend server.

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```
psql trivia < trivia.psql
```

### Running the server
From within the [`backend`](/backend) directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

The `--reload` flag will detect file changes and restart the server automatically.

## Getting Started - Frontend

### Installing Dependencies

### Tests and how to run them

## API Reference

