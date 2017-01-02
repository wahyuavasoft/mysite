from flask import render_template, flash, redirect, url_for, request
from app import app
import json,urllib, sys
import requests

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

@app.route('/home', methods=['GET', 'POST','DELETE'])
def index():
    if request.method =='POST': 
        url = "http://128.199.232.32/dbpost"
        payload = {'COUNTRY':request.form['t'], 'CURRENCY':request.form['d']}
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers) 
        return redirect(url_for('index'))
    if request.method =='DELETE': 
        url = "http://128.199.232.32/db/"+request.form['url']
        payload = ""
        headers = {'content-type': 'application/json'}
        response = requests.request("DELETE", url, data=payload, headers=headers)
        return redirect(url_for('index'))
    data = urllib.urlopen("http://128.199.232.32/db").read()
    resp_dict = json.loads(data)
    post=(resp_dict)
    return render_template('home.html',title='project',user=user,post=post)

@app.route('/input')
def input():
    z = [
    [ "Tiger Nixon", "System Architect", "Edinburgh", "5421", "2011/04/25", "$320,800" ],
    [ "Garrett Winters", "Accountant", "Tokyo", "8422", "2011/07/25", "$170,750" ],
    [ "Ashton Cox", "Junior Technical Author", "San Francisco", "1562", "2009/01/12", "$86,000" ],
    [ "Cedric Kelly", "Senior Javascript Developer", "Edinburgh", "6224", "2012/03/29", "$433,060" ],
    [ "Airi Satou", "Accountant", "Tokyo", "5407", "2008/11/28", "$162,700" ],
    [ "Brielle Williamson", "Integration Specialist", "New York", "4804", "2012/12/02", "$372,000" ],
    [ "Herrod Chandler", "Sales Assistant", "San Francisco", "9608", "2012/08/06", "$137,500" ],
    [ "Rhona Davidson", "Integration Specialist", "Tokyo", "6200", "2010/10/14", "$327,900" ],
    [ "Colleen Hurst", "Javascript Developer", "San Francisco", "2360", "2009/09/15", "$205,500" ],
    [ "Sonya Frost", "Software Engineer", "Edinburgh", "1667", "2008/12/13", "$103,600" ],
    [ "Jena Gaines", "Office Manager", "London", "3814", "2008/12/19", "$90,560" ],
    [ "Quinn Flynn", "Support Lead", "Edinburgh", "9497", "2013/03/03", "$342,000" ],
    [ "Charde Marshall", "Regional Director", "San Francisco", "6741", "2008/10/16", "$470,600" ],
    [ "Haley Kennedy", "Senior Marketing Designer", "London", "3597", "2012/12/18", "$313,500" ],
    [ "Tatyana Fitzpatrick", "Regional Director", "London", "1965", "2010/03/17", "$385,750" ],
    [ "Michael Silva", "Marketing Designer", "London", "1581", "2012/11/27", "$198,500" ],
    [ "Paul Byrd", "Chief Financial Officer (CFO)", "New York", "3059", "2010/06/09", "$725,000" ],
    [ "Gloria Little", "Systems Administrator", "New York", "1721", "2009/04/10", "$237,500" ],
    [ "Bradley Greer", "Software Engineer", "London", "2558", "2012/10/13", "$132,000" ],
    [ "Dai Rios", "Personnel Lead", "Edinburgh", "2290", "2012/09/26", "$217,500" ],
    [ "Jenette Caldwell", "Development Lead", "New York", "1937", "2011/09/03", "$345,000" ],
    [ "Yuri Berry", "Chief Marketing Officer (CMO)", "New York", "6154", "2009/06/25", "$675,000" ],
    [ "Caesar Vance", "Pre-Sales Support", "New York", "8330", "2011/12/12", "$106,450" ],
    [ "Doris Wilder", "Sales Assistant", "Sidney", "3023", "2010/09/20", "$85,600" ],
    [ "Angelica Ramos", "Chief Executive Officer (CEO)", "London", "5797", "2009/10/09", "$1,200,000" ],
    [ "Gavin Joyce", "Developer", "Edinburgh", "8822", "2010/12/22", "$92,575" ],
    [ "Jennifer Chang", "Regional Director", "Singapore", "9239", "2010/11/14", "$357,650" ],
    [ "Brenden Wagner", "Software Engineer", "San Francisco", "1314", "2011/06/07", "$206,850" ],
    [ "Fiona Green", "Chief Operating Officer (COO)", "San Francisco", "2947", "2010/03/11", "$850,000" ],
    [ "Shou Itou", "Regional Marketing", "Tokyo", "8899", "2011/08/14", "$163,000" ],
    [ "Michelle House", "Integration Specialist", "Sidney", "2769", "2011/06/02", "$95,400" ],
    [ "Suki Burks", "Developer", "London", "6832", "2009/10/22", "$114,500" ],
    [ "Prescott Bartlett", "Technical Author", "London", "3606", "2011/05/07", "$145,000" ],
    [ "Gavin Cortez", "Team Leader", "San Francisco", "2860", "2008/10/26", "$235,500" ],
    [ "Martena Mccray", "Post-Sales support", "Edinburgh", "8240", "2011/03/09", "$324,050" ],
    [ "Unity Butler", "Marketing Designer", "San Francisco", "5384", "2009/12/09", "$85,675" ]
    ]
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
    return render_template('input.html',title='project',user=user,isi=isi,z=z)

@app.route('/data')
def data():
    return render_template('data.html',title='project',user=user)

@app.route('/utility')
def utility():
    return render_template('utility.html',title='project',user=user)

@app.route('/acounting')
def acounting():
    n=0
    data = '{"jual":' \
       '[{"no":"001","Nama":"toyoo", "Barang": "jeruk", "Qty": "1", "harga":"100"},' \
        '{"no":"002","Nama":"gotoo", "Barang": "apel",  "Qty": "2", "harga":"200"},' \
        '{"no":"003","Nama":"momoo", "Barang": "mangga","Qty": "3", "harga":"300"},' \
        '{"no":"004","Nama":"mojoo", "Barang": "anggur","Qty": "4", "harga":"400"},' \
        '{"no":"005","Nama":"gotoo", "Barang": "cerry", "Qty": "5", "harga":"500"},' \
        '{"no":"006","Nama":"royoo", "Barang": "pisang","Qty": "6", "harga":"600"},' \
        '{"no":"007","Nama":"yoyoo", "Barang": "melon", "Qty": "7", "harga":"700"},' \
        '{"no":"008","Nama":"yogoo", "Barang": "nanas", "Qty": "8", "harga":"800"},' \
        '{"no":"009","Nama":"monoo", "Barang": "kiwi",  "Qty": "9", "harga":"900"},' \
        '{"no":"010","Nama":"moyoo", "Barang": "lemon", "Qty": "10","harga":"1000"},' \
        '{"no":"011","Nama":"goroo", "Barang": "tomat", "Qty": "11","harga":"1100"}]}';
    ab = json.loads(data)
    faktur = ab['jual']
    n = len (faktur)
    return render_template('acounting.html',title='project',user=user,faktur=faktur,n=n)



