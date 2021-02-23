from flask import Flask,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)

app = Flask (__name__) 
app.config [  'SQLALCHEMY_DATABASE_URI'] = 'postgresql: // webadmin: PEMgvr72410
app.config [' SQLALCHEMY_TRACK MODIFICATIONS '] = False  
db =SQLAlchemy (app)   
ma = Marshmallow (app)