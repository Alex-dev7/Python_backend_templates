## FastAPI Template

### Setup

- create a virtual environment `python -m venv venv` (if you use another name, adjust .gitignore)

- enable virtual env `source ./venv/bin/activate`

- install dependencies `pip install -r requirements.txt`

### COMMANDS

- Running Server: `uvicorn server:app` or `python server.py`

### CONFIG

All of the properties defined in the dictionary config/__init__.py can be imported and used throughout your project. Feel free to add more. If you want the properties to be read from a .env file make sure to pass the USE_DOTENV env variable. `USE_DOTENV=True python server.py`

### Routes

Routes are written in the controllers folder

### Models 

The models folder available if you decide to use an ORM

### Built in Documentation

/docs will have built in documentation

### Procfile

The Procfile for Heroku deployment is included