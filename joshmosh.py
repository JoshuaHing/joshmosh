#!/usr/bin/python3

from flask import Flask, render_template, session, request, url_for, redirect
from flaskext.markdown import Markdown
import os
import sqlite3

subject_list = ['COMP1521', 'COMP1531', 'COMP3411', 'COMP3821']
data = []
num_posts = 14

app = Flask(__name__)
Markdown(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    conn = create_connection('joshmosh.db')
    if request.method == 'POST':
        subject = request.form.get('subject', '')
        #new_post_contents = markdown2.markdown(request.form.get('new_post_contents', ''))
        new_post_contents = request.form.get('new_post_contents', '')
        post_id = request.form.get('post_id', '')
        
        #print('before =', new_post_contents)
        #new_post_contents = Markup(new_post_contents)
        #print('after =', new_post_contents)
        change_content(subject, new_post_contents, post_id, conn)
        
    for i in range(0, 4):
        data.append(get_content(subject_list[i], conn))
        
    return render_template('home.html', data=data, subject_list=subject_list, num_posts=num_posts)

@app.route('/edit', methods=['GET', 'POST'])  
def edit():
    subject = request.form.get('subject', '')
    post_id = request.form.get('post_id', '')
    post_contents = request.form.get('post_contents', '')
    return render_template('edit.html', subject=subject, post_id=post_id, post_contents=post_contents)

def change_content(subject, new_post_contents, post_id, conn):
    with conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE {0} SET Contents = '{1}' WHERE ID = {2}".format(subject, new_post_contents, post_id))
 
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
