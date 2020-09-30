#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 00:48:50 2020

@author: deviantpadam
"""


from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)

# app.jinja_env.globals.update(zip=zip)

conn = sqlite3.connect('db2.sqlite')
    
cur = conn.cursor()
cur.execute('SELECT * FROM fake_news')
results = cur.fetchall()


@app.route('/')
def main():
    global results
    
    length = len(results)
    if length%30==0:
    	last = length//30
    else:
    	last = (length//30)+1

    page = request.args.get('num')
    if not str(page).isnumeric():
        page=1
        page=int(page)
    if int(page)==1:
        n = '/?num='+str(int(page)+1)
        p = "#"
    elif int(page)==last:
        p = '/?num='+str(int(page)-1)
        n = "#"
    else:
        p = '/?num='+str(int(page)-1)
        n = '/?num='+str(int(page)+1)

    news = results[(int(page)-1)*30:int(page)*30]
    return render_template('index.html',news=news , next=n,prev=p,last=last)

@app.route('/temp')
def temp():
	return render_template('base.html')

if '__main__'==__name__:
    app.run()
    