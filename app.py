from flask import Flask
import psycopg2
import urllib.request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'


@app.route('/database')
def sdfsdfsdfsdf():
    
    try:
        conn = psycopg2.connect("dbname='postgres' host='localhost' user='postgres'  password='postgres' port='5432'")
        cur = conn.cursor()
        cur.execute("""SELECT 1;""")
        rows = cur.fetchall()
        return str(rows)
    except Exception as e:
        return repr(e)

@app.route('/database2')
def sdfsdfsddhbfgbnrtfsdf():
    
    try:
        conn = psycopg2.connect("dbname='template1' host='172.17.0.2' user='postgres' password='postgres' port='5432'")
        cur = conn.cursor()
        cur.execute("""SELECT 1;""")
        rows = cur.fetchall()
        return str(rows)
    except Exception as e:
        return repr(e)
@app.route('/database3')
def sdfsdfsddhbfgbnrtffdgdfgsdf():
    
    try:
        conn = psycopg2.connect("dbname='template1' host='172.17.0.1' user='postgres' password='postgres' port='5432'")
        cur = conn.cursor()
        cur.execute("""SELECT datname from pg_database;""")
        rows = cur.fetchall()
        return str(rows)
    except Exception as e:
        return repr(e)


@app.route('/http')
def sdfsdfsdfsdfyxcyxcyxsdfsdf():

    contents = urllib.request.urlopen("http://localhost:5432").read()
    return contents
    

@app.route('/http2')
def sdfsdfsdfsxcxcvxcxxcdfsdfsdf():
    contents = urllib.request.urlopen("http://127.17.0.1:5432").read()
    return contents
        

@app.route('/ping')
def sdfsdfxcvxcvxcvsddsfsdfsdffsdfsdfsdf():
    return "pong"
    