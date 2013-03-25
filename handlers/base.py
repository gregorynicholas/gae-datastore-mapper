import webapp2
from webapp2_extras import jinja2


class BaseHandler(webapp2.RequestHandler):
    """
    BaseHandler for all request RequestHandlers
    """
    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, context=None):
        context = context or {}

        extra_context = {
            'request': self.request,
            'uri_for': self.uri_for,
        }

        # Only override extra context stuff if it's not set by the template:
        for key, value in extra_context.items():
            if key not in context:
                context[key] = value

        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)
