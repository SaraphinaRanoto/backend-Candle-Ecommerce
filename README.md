# backend-Candle-Ecommerce
E-Commerce site for Candles
The site consists of a backend and frontend part.
Database I used PostgreSql(PgAdmin4)
For the backend there are three files which are:
class.py---> this is where im getting products
dbclass.py--> connected the database with python
api.py---> connect our backend to frontend
The guide to using the backend(IN CANDLE FOLDER), run the following on the terminal in the api.py file
   $env:FLASK_APP = "api" -----> set the environment to use file name,
   $env:FLASK_ENV="development"  --------> for the server to restart,
    py -m flask run   --------> run code to reach endpoint 
