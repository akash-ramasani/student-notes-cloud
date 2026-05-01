# Installation and Execution Guide

To run this project you need to follow these steps. Make sure you have python installed on your computer.

## Requirements
You need these things:
* Python 3
* pip
* AWS account for S3 and Cognito
* MySQL database (local or RDS)

## Setup Steps
1. First get the source code folder.
2. Open the terminal and go to the project folder.
3. You should make a virtual environment so things dont break. Run `python -m venv .venv`.
4. Activate it with `source .venv/bin/activate`.
5. Now install all the libraries with `pip install -r requirements.txt`.
6. You need to make a `.env` file and put your AWS keys and database info there. Use the template I provided.
7. To make the database tables run `python migrate_db.py`.

## Running the App
After you do all steps just run this command:
`python app.py`

The app will start on port 5001. You can go to `localhost:5001` in your browser to see the website. If you are on EC2 then use the public IP of the server.
