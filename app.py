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

client = MongoClient(environ.get("MONGO_CONNECTION_STRING"))
db = client["testing"]['movement_range_raw']


@app.route('/data/daily')
@cache.cached(timeout=5000)
def daily_time_series():
    res = db.find({})
    return dumps(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
