import webapp2
import routes
import config

import lib_import
# # add the lib folder to the sys.path
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

app = webapp2.WSGIApplication(
    debug=config.debug,
    config=config.webapp2_config)

routes.add_routes(app)
