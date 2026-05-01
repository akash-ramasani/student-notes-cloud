HOW TO RUN MY PROJECT

Follow these steps to get my app running on your computer:

WHAT YOU NEED
python 3 installed
your aws keys s3 cognito etc
mysql database

STEPS TO SETUP
1 open project folder in terminal
2 make virtual environment: python m venv venv
3 activate it: source venv bin activate
4 install all libraries: pip install r requirements txt
5 make env file and put aws and db info there: i included template for you
6 run python migrate db py to make database tables

STARTING APP
Just run python app py:
app will start on localhost 5001: you can open this in browser to see my project: for production i used nginx to point notecloud akashramasani com to this port
