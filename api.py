#py.exe -m pip install Flask  -------> to install flask
#$env:FLASK_APP = "api" -----> set the environment to use file name
# $env:FLASK_ENV="development"  --------> for the serer to restart
# py -m flask run   --------> run our code to reach endpoint
    
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
import dbClass
    
app = Flask(__name__)

ALLOWED_ORIGINS = ['localhost', '127.0.0.1']

cors = CORS(app, resources ={"/*": {"origins" : ALLOWED_ORIGINS }})


@app.route("/candles/")
@cross_origin(support_credentials = True)
def candle_endpoint():
    pTable = dbClass.candlesTable 

    pRows =pTable.select("*")
    product = []

    for row in pRows:
        tmp_product = {
            "id_num" : row[0],
            "candle_name" : row[1],
            "candle_color" : row[2],
            "quantity" : row[3],
            "price" : row[4],
        }

        product.append(tmp_product)

    pDict = {
        "product" : product
    }

    return jsonify(pDict)


@app.route("/candles/<id_num>") 
@cross_origin(support_credentials = True)
def candles_endpoint(id_num):
    pTable = dbClass.candlesTable 


    pRows =pTable.select("*", "id_num = " + id_num)

    candles = {
            "id_num" : pRows[0][0],
            "candle_name" : pRows[0][1],
            "candle_color" : pRows[0][2],
            "quantity" : pRows[0][3],
            "price" : pRows[0][4],
        }

    return jsonify(candles)


@app.route("/customer/")
def customer_endpoint():
    cTable = dbClass.customerTable

    cRows = cTable.select("*")
    customer = []

    for row in cRows:
        tmp_customer = {
            "customer_id":  row[0],
         "customer_name":  row[1]
        }

        customer.append(tmp_customer)

        cDict = {
            "customer" : customer
        }
        
        return jsonify(cDict)

