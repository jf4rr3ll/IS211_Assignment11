#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 11 Module"""

from flask import Flask, request, redirect, render_template
import re
import pickle

app = Flask(__name__)
toDo = []
emailCheck = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

@app.route('/')
def loadPage():
    return render_template('index.html', toDo=toDo)


@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    if re.match(emailCheck, email) is None:
        return redirect('/')
    elif priority not in ('low', 'medium', 'high'):
        return redirect('/')
    else:
        toDo.append((email, task, priority))
        return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    toDo = []
    return redirect('/')


@app.route('/save', methods=['POST'])
def save():
    pickle.dump(toDo, open('toDo.txt', 'wb'))
    return redirect('/')

if __name__ == '__main__':
    app.run()