import json
from flask import Flask, request
import uuid
import codecs
import base64


def create_app():
    app = Flask(__name__)

    @app.route("/hello")
    def hello():
        return{
            'msg': 'Hey there!'
        }

    @app.after_request
    def enable_cors(response):
        header = response.headers
        header['Access-Control-Allow-Origin'] = '*'
        header['Access-Control-Allow-Headers'] = '*'
        return response

    return app

if __name__ == '__main__':
    app = create_app()
    context = ('cert.pem', 'key.pem')#certificate and key files
    app.run(debug=True, ssl_context=context, host='0.0.0.0', port=5001)