# flask is a highly customizable microservice built in to Python, used to routing and request handling



from flask import Flask, request, jsonify
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#to be change
db_config = {
  'host': 'hostname',
  'user': 'username',
  'password': 'password',
  'database': 'database'
}

def get_connection():
  return pymysql.connect(**db_config)