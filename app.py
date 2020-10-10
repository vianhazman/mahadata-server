from flask import Flask, jsonify
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
client = MongoClient('mongodb://10.119.105.232:27017/', username='root', password='rootpassword')
db = client["testing"]

@app.route('/data/rank/')
@cache.cached(timeout=5000)
def get_rank():
    col = db['movement_range_district']
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
