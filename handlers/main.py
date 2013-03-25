from handlers.base import BaseHandler


class MainHandler(BaseHandler):

    def get(self):
        template_values = {
            'key': 'value'
        }

        self.render_response('main.html', template_values)
