# Full Stack Trivia API Project

This project is a demonstration of how to develop and use API and API documentation with the main goal to build a trivia API. Trivia is an game app that allows to:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

By completing this trivia app, various abilities such as to structure plan, implement, and test an API are demonstrated - skills essential for enabling any future applications to communicate with others.

## Getting Started - Frontend
The frontend is designed to work with [Flask-based Backend](/backend). First the backend needed to be developed, the code tested using Postman or curl and the endpoints in the frontend updated, then the frontend should integrate smoothly.

### Installing Dependencies

1. **Installing Node and NPM**
  <br>This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from https://nodejs.com/en/download.

2. **Installing project dependencies**
  <br>This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the [`frontend`](/frontend) directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```
  tip: **npm** i is shorthand for **npm install**
  
### Running Your Frontend in Dev Mode
The frontend app was built using create-react-app. In order to run the app in development mode use npm start. You can change the script in the package.json file.

Open http://localhost:3000 to view it in the browser. The page will reload if you make edits.

```bash
npm start
```

## Getting Started - Backend

### Installing Dependencies
1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the python docs

2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the [`backend`](/backend) directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the [`requirements.txt`](/backend/requirements.txt) file.

4. **Key Dependencies**
- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight PostgreSQL database. You'll primarily find code related to the database in the `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) is the extension we'll use to handle cross origin requests from our frontend server.

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```bash
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

### Testing
To run the tests, run

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.
- Authentication: This version of the application does not require authentication or API keys.

### Error Handling
Errors are returned as JSON objects in the following format:

```
TODO: Add the format
```

The API will return the following error types when requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable

### Endpoints

#### GET /categories

- General: 
  - Returns a list of categories

- Sample: 
  - `curl http://127.0.0.1:5000/categories`

```
TODO: Add the HTTP response for categories
```
