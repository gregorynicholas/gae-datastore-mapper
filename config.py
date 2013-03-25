from google.appengine.api import app_identity
import logging
import os

app_name = "gae-datastore-mapper"
app_id = app_identity.get_application_id()
isDev = os.environ['SERVER_SOFTWARE'].startswith('Dev')
isLocal = isDev
debug = isDev

webapp2_config = {}
webapp2_config['webapp2_extras.sessions'] = {
    'secret_key': 'ajsdlkhandnaisdnoainsdiands',
}

webapp2_config['webapp2_extras.auth'] = {
    'user_model': 'models.models.User',
    'cookie_name': 'session_name'
}

webapp2_config['webapp2_extras.jinja2'] = {
    'template_path': 'templates'
}

error_templates = {
    403: 'errors/default_error.html',
    404: 'errors/default_error.html',
    500: 'errors/default_error.html',
}

#: LOCAL ENVIRONMENT overrides all
if (isLocal):
    # define environment specific configuration
    localhost = True
    logging.info('Using localhost configuration in config.py.')

else:

    if (app_id == 'application_id'):
        #: PROD ENVIRONMENT
        localhost = False

    if (app_id == 'application_id_dev'):
        #: DEV ENVIRONMENT
        localhost = False

    if (app_id == 'application_id_qa'):
        #: QA ENVIRONMENT
        localhost = False
