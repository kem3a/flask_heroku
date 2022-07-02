from datetime import timedelta

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item, Items
from resources.store import Store, Stores
from resources.user import UserRegister
from security import authenticate, identity

from db import db

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config["JWT_EXPIRATION_DELTA"] = timedelta(hours= 0.5)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.secret_key = "eWMzNnNDTEQxWEFlWVFydGc1SVRFU3BqSXNTampSeCFBJUQqRy1LYVBkJiR6YWdTZ1ZrNHQ3dyF6JUMqRi1KYU5kUm1acTN0Nnc5eiRDJkZKQFNoVm1ZcTNzNnY5eSRCJkVhUGRTZ1ZrWXAzczV2OHkv"
api = Api(app)

jwt = JWT(app, authenticate, identity)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Items, "/items")
api.add_resource(Stores, "/stores")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(Store, "/store/<string:name>")    
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    
    
    app.run()
