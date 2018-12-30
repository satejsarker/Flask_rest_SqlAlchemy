import os
from flask import Flask
from flask_restful import  Api
from flask_jwt import  JWT
from Security import  authenticate,identity
from resources.user import  UserResgister
from resources.item import Items , IteamList
from resources.store import Store,  StoreList
from db import db


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("DATABASE_URL",'sqlite:///data.db')
# app.config['SQLALCHEMY_DATABASE_URI']="postgres://dqcrbfxljsveyw:5fd483575d7a4636f01520281355ab33669f086a55ed45c5b6bc183020f20e61@ec2-174-129-25-182.compute-1.amazonaws.com:5432/d2q03dj06v3gcq"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='satej@)((!!!klnvlknsdfiasdasdmnnjan$$%'

@app.before_first_request
def create_table():
    db.create_all()

api=Api(app)
jwt=JWT(app,authenticate,identity)

##demo in maemory data
#Route
db.init_app(app)
api.add_resource(Items,'/iteam/<string:name>')
api.add_resource(IteamList,'/iteams')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/storelist')
api.add_resource(UserResgister,'/register')
if __name__ == '__main__':
    from db import  db
    db.init_app(app)
    app.run(port=5000)
