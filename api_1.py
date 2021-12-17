from flask import Flask,jsonify ,Request
from flask_restful import Api

app=Flask(__name__)
# api=Api(app)
@app.route('/details/<data>')

def details(data):
    data={'123.123.123.123':'ip address','user':"sagar",'details' :'engineer'}
    return data
    
    
app.run(debug=True)    