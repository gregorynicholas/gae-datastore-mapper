from google.appengine.ext import ndb

from wtforms import Form
from wtforms import TextField
from wtforms import BooleanField
from wtforms import validators


class ResourceModel(ndb.Model):
    """
    A simple Resource Model
    """
    id = ndb.IntegerProperty(required=True)
    name = ndb.StringProperty(required=True)
    description = ndb.TextProperty()
    actve = ndb.BooleanProperty()


class ResourceForm(Form):
    """
    A simple ResourceForm
    """

    id = TextField(label='Resource ID',
                   validators=[validators.required(), validators.length(max=10)],
                   description='This is the id of the resource.')

    name = TextField(label='Resource Name',
                     validators=[validators.required(), validators.length(max=10)],
                     description='This is the name of the resource.')

    description = TextField(label='Resource Description',
                            validators=[validators.required(), validators.length(max=10)],
                            description='This is the description of the resource.')

    active = BooleanField(label='Active',
                          description='This determines if the resource is active.')
