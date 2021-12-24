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
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://lyveomvzcylbnf:4d195a169155b005a5d890af00ebeaaa087d17710697054a86fc6a55bfd8a859@ec2-50-19-160-40.compute-1.amazonaws.com:5432/d679q2q8nlq55k'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)