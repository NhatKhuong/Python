from flask import Flask
from flask_restful import Resource, Api
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class HelloWorld(Resource):
    def get(self):

        _res = requests.post('https://finance.vietstock.vn/company/tradinginfo',
                        headers={
                            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
                        },
                        cookies={
                            "__RequestVerificationToken": "XTIJqg6nv9qd5jazSpJsFeef5E6mOmOWAGdP6cP9CQkoDayp_agtS9wTGMBoFOD2OGdH1Bq7JVKHubdjPQHnx2PNUsa-L0d1o32DQIVK-PI1",
                            "ASP.NET_SessionId": "v0ct31jt14gft4fkxx0i2vye",
                            "language": "vi-VN"
                        },
                        data={
                            "code": "VNM",
                            "s": "0",
                            "t": "",
                            "__RequestVerificationToken": "bx-iabZXI1TIAkI4_J0Cmz5Bb2_sru91ot_TXq8nd0JNxhjOIr9UOzeZNBj3Bmw5fMNH6_Iw-b47M5KsCf2pQeW_s-hL6a28_y3I_ghgX9g1"
                        }
                    )
        return _res.json()

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)