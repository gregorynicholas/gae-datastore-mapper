from handlers.base import BaseHandler


class TemplateHandler(BaseHandler):
    def get(self, template_name):

        template_values = {
            'key': 'value'
        }

        self.render_response(template_name + '.html', template_values)
