from flask import Flask, request, Response
import json



app = Flask(__name__)

@app.route('/animals', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def method_handler():
    if (request.method == 'GET'):
        params = request.args
        resp = {
            "animal" : "Lion",
            "animal" : "Tiger",
            "animal" : "Bear",
            "animal" : "Rhino"
        }
        print(params)
        return Response(json.dumps(resp),
                        mimetype="application/json",
                        status=200)
    
    elif (request.method == "POST"):
        data = request.json
        resp = {
            "animal" : "Snake"
        }
        print(data)
        if(data.get('animals')!= None):
            print(data.get('animals'))
        else:
            print("Did not recieve animal")
        return Response(json.dumps(resp),
                        mimetype="application/json",
                        status=200)
    elif (request.method == "PATCH"):
        params = request.args
        resp = {
            "animal" : "Siberian Tiger"
        }
        print(params)
        return Response(json.dumps(resp),
                        mimetype="application/json",
                        status=200)
    else: (request.method == "DELETE")
    params= request.args
    request.delete(params)
    exit()

