import pymysql

pymysql.install_as_MySQLdb()

from flask import Flask
from app.views import route
from app.json_encoder import AlchemyEncoder

app = Flask(__name__)
app.json_encoder = AlchemyEncoder

route(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
