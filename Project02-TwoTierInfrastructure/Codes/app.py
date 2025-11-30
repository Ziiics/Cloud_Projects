# flask is a highly customizable microservice built in to Python, used to routing and request handling
# pymysql integrate Python and MySQL
# flask CORS integrate the falsk fucntionality with the backend

from flask import Flask, request, jsonify, render_template,redirect, url_for
import pymysql, boto3, mysql.connector
from flask_cors import CORS
from datetime import date

app = Flask(__name__)
CORS(app)

# get pasword from SSM
def get_ssm_secure_string():
  # REPLACE region_name TO THE REGION OF YOUR EC2
  ssm_client = boto3.client('ssm',region_name = 'us-east-1')
  try:
    response = ssm_client.get_parameter(
      # REPLACE Name TO THE NAME LISTED FOR THIS PROJECT IN Parameter store
      Name ='/project2/rds_password',
      WithDecryption = True
    )
    return response['Parameter']['Value']
  except Exception as e:
    print(f"Error retrieving parameter '/project2/rds_password': {e}")
    return None

# Replace these values to indicate values
# host = endpoint rds of this project
# user = the user chosen with highest permission for this project, the listed user in IAM
# database = the name of dataabse when doing CREATE DATABASE
db_config = {
  'host': 'project2-database.cgpcgg00cq2s.us-east-1.rds.amazonaws.com',
  'user': 'admin',
  'password': get_ssm_secure_string(),
  'database': 'purpose'
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
        "SELECT * FROM visit_purpose"
      )
      cursor.execute(query)
      visitors = cursor.fetchall()

    return jsonify({'visitors': visitors})
  except Exception as e:
    return jsonify({'visitors': []})
  finally:
    connection.close()

@app.route('/', methods=['GET','POST'])
def home():
  connection = get_connection()

  try:
    if request.method == 'POST':
      name = request.form['name']
      purpose = request.form['purpose']
      with connection.cursor() as cursor:
        cursor.execute = (
          "INSERT INTO visit_purpose (name, purpose) VALUES (%s, %s)",
          (name, purpose)
        )
        connection.commit()
    
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
      query = (
        "SELECT * FROM visit_purpose"
      )
      cursor.execute(query)
      visitors = cursor.fetchall()
    
    today = date.today().strftime('%Y-%m-%d')
    return render_template('index.html', today=today, visitors=visitors)
  finally:
    connection.close()


@app.route('/delete_visitors/<int:id>', methods=['DELETE'])
def delete_visitor(id):
  connection = get_connection()

  try:
    with connection.cursor() as cursor:
      query = (
        "DELETE FROM visit_purpose WHERE id = %s"
      )
      cursor.execute(query,(id,))
      connection.commit()
    return redirect(url_for('home'))
  except Exception as e :
    print(e)
    return jsonify({'success': False})
  finally:
    connection.close()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
