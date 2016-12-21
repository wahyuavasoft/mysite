from flask import render_template, flash, redirect, url_for, request
from app import app
import json,urllib, sys

user = {'name': '</python>'}

@app.route('/', methods = ['GET','POST'])
def login():
    error=None
    if request.method =='POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error='user/pass salahhhhh'
        else:
            return redirect(url_for('index'))
    return render_template("index.html",error=error,user=user)

@app.route('/home')
def index():
    return render_template('home.html',title='project',user=user)

@app.route('/input')
def input():
    data = '{'\
      '"Barang":' \
        '['\
        '{"Nama": "TOYO", "Qty": "19",  "harga":"1.000",     "total":"19.000",   "id":"1"},'   \
        '{"Nama": "MOMO", "Qty": "3",   "harga":"3.000",     "total":"9.000",    "id":"2"},'   \
        '{"Nama": "MOJO", "Qty": "77",  "harga":"1.000",     "total":"77.000",   "id":"3"},'   \
        '{"Nama": "GOTO", "Qty": "12",  "harga":"2.000",     "total":"24.000",   "id":"4"},'   \
        '{"Nama": "LOMO", "Qty": "8",   "harga":"5.000",     "total":"40.000",   "id":"5"},'   \
        '{"Nama": "JOJO", "Qty": "1",   "harga":"55.000",    "total":"55.000",   "id":"6"},'   \
        '{"Nama": "TOTO", "Qty": "14",  "harga":"500",       "total":"12.000",   "id":"7"},'   \
        '{"Nama": "DOJO", "Qty": "14",  "harga":"500",       "total":"12.000",   "id":"8"},'   \
        '{"Nama": "MOMO", "Qty": "3",   "harga":"3.000",     "total":"9.000",    "id":"9"},'   \
        '{"Nama": "MOJO", "Qty": "77",  "harga":"1.000",     "total":"77.000",   "id":"10"},'  \
        '{"Nama": "GOTO", "Qty": "12",  "harga":"2.000",     "total":"24.000",   "id":"11"},'  \
        '{"Nama": "LOMO", "Qty": "8",   "harga":"5.000",     "total":"40.000",   "id":"12"},'  \
        '{"Nama": "JOJO", "Qty": "1",   "harga":"55.000",    "total":"55.000",   "id":"13"},'  \
        '{"Nama": "TOTO", "Qty": "14",  "harga":"500",       "total":"12.000",   "id":"14"},'  \
        '{"Nama": "DOJO", "Qty": "14",  "harga":"500",       "total":"12.000",   "id":"15"},'  \
        '{"Nama": "NOMO", "Qty": "5",   "harga":"6.000",     "total":"30.000",   "id":"16"}'   \
        ']'\
            '}';
    zz = json.loads(data)
    isi=zz['Barang']
    return render_template('input.html',title='project',user=user,isi=isi)

@app.route('/data')
def data():
    return render_template('data.html',title='project',user=user)

@app.route('/utility')
def utility():
    return render_template('utility.html',title='project',user=user)

@app.route('/acounting')
def acounting():
    return render_template('acounting.html',title='project',user=user)



