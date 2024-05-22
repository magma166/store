from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="Pid",  
  password="Mag19042006",
  database="shop"   
)

mycursor = mydb.cursor()

@app.route('/')
def registration():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        val = (username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return "Регистрация успешна"

if __name__ == '__main__':
    app.run(debug=True)
