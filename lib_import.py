import os
import sys

# add the lib folder to the sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))


from wtforms import validators, widgets
from wtforms.fields import *
from wtforms.form import Form
from wtforms.validators import ValidationError
