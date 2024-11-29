from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
import cloudinary




app = Flask(__name__)
app.secret_key = 'aewuge124g1724by812hb'
app.config["SQLALCHEMY_DATABASE_URI"] ='mysql+pymysql://root:%s@localhost/it01_saledbv1?charset=utf8mb4' %quote ('12345')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

cloudinary.config(cloud_name='dnpodiilj',
                  api_key='874131819545712',
                  api_secret='xHDsHPIIbwKkoT6qfPYTAvn4pmA')

db = SQLAlchemy(app)

login = LoginManager(app=app)




