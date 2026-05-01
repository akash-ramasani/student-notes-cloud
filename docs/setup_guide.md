# How to run my project

Follow these steps to get my app running on your computer.

## What you need
* Python 3 installed
* Your AWS keys (S3, Cognito, etc.)
* A MySQL database

## Steps to setup
1. Open the project folder in your terminal.
2. Make a virtual environment: `python -m venv .venv`.
3. Activate it: `source .venv/bin/activate`.
4. Install all the libraries: `pip install -r requirements.txt`.
5. Make a `.env` file and put your AWS and DB info there. I included a template for you.
6. Run `python migrate_db.py` to make the database tables.

## Starting the app
Just run `python app.py`. 
The app will start on `localhost:5001`. You can open this in your browser to see my project.
