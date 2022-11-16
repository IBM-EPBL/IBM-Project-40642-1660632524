import ibm_db
from flask import Flask

app = Flask(__name__)

dictionary = {}
def printTableData(conn):
 sql = "SELECT * FROM user details"
 out = ibm_db.exec_immediate(conn, sql) 
 document =ibm_db.fetch_assoc(out)
 while document != False:
  dictionary.update({document['USERNAME']: document['PASSWORD']})
  document =ibm_db.fetch_assoc(out)
def insertTableData(conn, rollno, username, email, password):
  sql ="INSERT_INTO_userdetails(rollno, username, email, password)VALUES({},'{}','{}','{}')".format(rollno, username, email, password)
  out =ibm_db.exec_immediate(conn, sql)
  print('Number of affected rows:', ibm_db.num_rows(out), "\n")
def updateTableData(conn, rollno, username, email, password):
   sql = "UPDATE userdetails SET(username, email, password) = ('{}', '{}', '{}')WHERErollno = {}".format(username, email, password, rollno)
   out = ibm_db.exec_immediate(conn, sql)
   print('Number of affected rows : ', ibm_db.num_rows(out), "\n")
def deleteTableData(conn, rollno):
   sql = "DELETE FROM userdetails WHERErollno={}".format(rollno)
   out = ibm_db.exec_immediate(conn, sql)
   print('Number of affected rows: ', ibm_db.num_rows(out), "\n")
try:
      conn = ibm_db.connect("DATABASE=bludbHOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud  PORT=31198SECURITY=SSL SSLServerCertificate=DigiCertGlobalRootCA.crtPROTOCOL=TCPIP UID=bjn03696 PWD=ef96tLJX2VjzaCPX", "","")
      print("Db connected")
except:
       print("Error")
Flask, render_template, request, url_for, sessionapp = Flask(__name__)
username = request.form['username']
password = request.form['password']


@app.route("/")
@app.route("/login", methods=['POST', 'GET'])
def login():
 if():
      request.method=="POST"
      printTableData(conn)

    
