# flask is a highly customizable microservice built in to Python, used to routing and request handling
# pymysql integrate Python and MySQL
# flask CORS integrate the falsk fucntionality with the backend

from flask import Flask, request, jsonify
import pymysql, boto3, mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# get pasword from SSM
def get_ssm_secure_string():
  ssm_client = boto3.client('ssm',region_name = 'us-east-1')
  try:
    response = ssm_client.get_parameter(
      Name ='/project2/rds_password',
      WithDecryption = True
    )
    return response['Parameter']['Value']
  except Exception as e:
    print(f"Error retrieving parameter '/project2/rds_password': {e}")
    return None

db_config = {
  'host': 'project2-database.cgpcgg00cq2s.us-east-1.rds.amazonaws.com',
  'user': 'admin',
  'password': get_ssm_secure_string(),
  'database': 'database'
}

#connect python and mysql using db_config information
def get_connection():
  return pymysql.connect(**db_config)

# part of necessity from flask itself
@app.route('/add_visitor', methods=['POST'])
def add_visitor():
  connection = get_connection()
  try:
    name = request.json['name']
    purpose = request.json['purpose']
    
    with connection.cursor() as cursor:
      query = (
        "INSERT INTO visit_purpose (name, purpose)"
        "VALUES (%s, %s)"
        )
      data = (name, purpose)
      cursor.execute(query, data)
      connection.commit()

    return jsonify({'success':True})
  except Exception as e:
    return jsonify({'success': False})
  finally:
    connection.close()


@app.route('/get_visitors')
def get_visitor():
  connection = get_connection()

  try:
    with connection.cursor() as cursor:
      query = (
        "SELECT * FROM visitors"
      )
      cursor.execute(query)
      visitors = cursor.fetchall()

    return jsonify({'visitors': visitors})
  except Exception as e:
    return jsonify({'visitors': []})
  finally:
    connection.close()


@app.route('/delete_visitors/<int:id>', methods=['DELETE'])
def delete_visitor(id):
  connection = get_connection()

  try:
    with connection.cursor() as cursor:
      query = (
        "DELETE FROM visitors WHERE id = %s"
      )
      cursor.execute(query,(id,))
      connection.commit()
    return jsonify({'success': True})
  except Exception as e :
    print(e)
    return jsonify({'success': False})
  finally:
    connection.close()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)