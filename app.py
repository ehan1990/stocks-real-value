import datetime
import logging

from flask import Flask, jsonify, request
from flask_cors import CORS

from libs import constants
from libs import stock_service
from libs.mongo_service import MongoService
from libs.constants import DB_NAME

"""
CRUD records
ACL on IAM

"""


app = Flask(__name__)
CORS(app)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(filename)s:%(lineno)d %(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


@app.route("/healthcheck", methods=["GET"])
def healthcheck_endpoint():
    data = {
        "msg": f"Running version {constants.VERSION}",
        "date": f"{datetime.datetime.utcnow().isoformat()[0:19]}Z",
    }
    return jsonify(data)


@app.route("/stocks/<ticker>", methods=["GET"])
def one_stock_endpoint(ticker):
    stock = stock_service.get_one_stock(ticker)
    return jsonify(stock.__dict__)


def main():
    MongoService.init(DB_NAME)
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)


if __name__ == "__main__":
    main()
