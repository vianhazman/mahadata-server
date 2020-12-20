import operator

from flask import Flask, jsonify, request, Response
from bson.json_util import dumps
from flask_caching import Cache
from pymongo import MongoClient
from flask_compress import Compress
from flask_cors import CORS
from dotenv import load_dotenv
from os import path, environ

load_dotenv(path.join(path.dirname(__file__), '.env'))

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': environ.get("REDIS_CONNECTION_STRING")})
Compress(app)
CORS(app)
client = MongoClient(environ.get("MONGO_CONNECTION_STRING"))
db = client["testing"]

def generate_time_series_csv(db_name):
    collection = db[db_name]
    cursor = collection.find({})
    base='date,region,ratio,change\n'
    for document in cursor:
        date = document['date']
        data = document['data']
        transformed = []
        for k,v in data.items():
            row = "{},{},{},{}\n".format(date,k,v["ratio"],v["change"])
            base += row
    return base

def generate_case_csv(db_name):
    collection = db[db_name]
    cursor = collection.find({})
    base='date,region,new_cases\n'
    for document in cursor:
        date = document['date']
        data = document['data']
        transformed = []
        for k,v in data.items():
            row = "{},{},{}\n".format(date,k,v)
            base += row
    return base

@app.route('/data/rank/<area_type>')
@cache.cached(timeout=5000)
def get_rank(area_type):
    col_name = 'rank_{}'.format(area_type)
    col = db[col_name]
    res = col.find({})
    return dumps(res)

@app.route('/data/daily/district')
@cache.cached(timeout=5000)
def district_time_series():
    col = db['movement_range_district']
    res = col.find({})
    return dumps(res)


@app.route('/data/daily/province')
@cache.cached(timeout=5000)
def province_time_series():
    col = db['movement_range_province']
    res = col.find({})
    return dumps(res)


@app.route('/data/case/province/')
@cache.cached(timeout=5000)
def province_daily_case():
    col = db['historical_case']
    res = col.find({})
    return dumps(res)

@app.route('/data/case/province/download/'+environ.get("SECRET_PATH"))
def province_daily_case_download():
    csv_str = generate_case_csv('historical_case')
    return Response(
        csv_str,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=kasus_harian_provinsi.csv"})


@app.route('/data/daily/district/download/'+environ.get("SECRET_PATH"))
def district_time_series_download():
    csv_str = generate_time_series_csv('movement_range_district')
    return Response(
        csv_str,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=mobilitas_kabkot.csv"})

@app.route('/data/daily/province/download/'+environ.get("SECRET_PATH"))
def province_time_series_download():
    csv_str = generate_time_series_csv('movement_range_province')
    return Response(
        csv_str,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=mobilitas_provinsi.csv"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ.get("RUNNING_PORT"))
