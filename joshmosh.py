#!/usr/bin/python3

from flask import Flask, render_template, session, request, url_for, redirect
import os
import sqlite3

subject_list = ['COMP1521', 'COMP1531', 'COMP3411', 'COMP3821']
num_posts = 14

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    conn = create_connection('joshmosh.db')
    data = get_content(subject_list[0], conn)
    return render_template('home.html', data=data, subject_list=subject_list, num_posts=num_posts)

def get_content(subject, conn):
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM {0}".format(subject))
        data = cursor.fetchall()
        return data
        
    
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
  
    
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, use_reloader=True, port=11138)
