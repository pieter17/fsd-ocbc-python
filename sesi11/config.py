import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
#     basedir, 'people.db')
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://owxbulbvuiwhfh:01f0f986a93cdf56af59f95aaa14e23a48aad8860c19dc13ac13b8289def6b0b@ec2-52-71-217-158.compute-1.amazonaws.com:5432/d2uf38i9sdgl27'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)