import webapp2
import logging

from wtforms.ext.appengine.ndb import model_form

from handlers.base import BaseHandler
from models.resource import ResourceModel


class ResourceHandler(BaseHandler):
    """
    ResourceHandler Reference

    There are 7 standard methods:
        index - GET /resources/
        show - GET /resources/{id}/
        edit - GET /resources/{id}/{action}/
        new - GET /resources/new/
        create - POST /resources/
        update - POST/PUT /resources/{id}/{action}/
        delete - POST/DELETE /resources/{id}/{action}/

    """
    @webapp2.cached_property
    def form(self):
        """
        Reference to the WTForm object

        This is used to inject self.form
        into the template context.
        """
        # Generate a form based on the model.
        ResourceModelForm = model_form(ResourceModel)
        # create and return an instance of the form based on
        # the ResourceModel
        return ResourceModelForm

    def index(self):
        """
        Index method

        Display a list of resources

        """

        context = {
            'action': 'Index',
            'form': None,
            'submit_routename': '#'
        }

        self.render_response('resource.html', context=context)

    def new(self):
        """
        New method

        Gather input to create a new resource

        """
        resource_model_form = model_form(ResourceModel)
        form = resource_model_form(self.request.POST)

        context = {
            'action': 'New',
            'form': form,
            'submit_routename': 'resource.create'
        }

        self.render_response('resource.html', context)

    def create(self):
        """
        Create method

        Create a new resource using posted data

        """
        # create form instance from the ResourceModel
        resource_model_form = model_form(ResourceModel)
        form = resource_model_form(self.request.POST)

        context = {
            'action': 'New',
            'form': form,
            'submit_routename': 'resource.create'
        }

        # since this method is only called from a post,
        # we do not need to check for request.method == "POST"
        # if self.form.validate() returns true, then save
        # the data
        if form.validate():
            logging.debug('Form Validated!')
            entity = ResourceModel()
            # push form values into model
            form.populate_obj(entity)
            # save to data store
            key = entity.put()
            # redirect to index and/or edit form with new id
            logging.debug('key={0}'.format(key))
            # redirect to the edit page for the created id
            return webapp2.redirect_to('resource.edit', id=key.id())

        # the form did not validate, redisplay with errors
        return self.render_response('resource.html', context)

    def show(self, id):
        """
        Show method

        Show a specific resource by id

        """
        context = {
            'action': 'Show',
            'id': id
        }

        self.render_response('resource.html', context)

    def edit(self, id):
        """
        Edit method

        Edit a specific resource by id

        """
        entity_id = int(id)
        resource_model_form = model_form(ResourceModel)
        entity = ResourceModel.get_by_id(entity_id)
        form = resource_model_form(self.request.POST, obj=entity)

        context = {
            'action': 'Edit',
            'id': id,
            'form': form,
            'submit_routename': 'resource.update'
        }

        self.render_response('resource.html', context)

    def update(self, id):
        """
        Update method

        Update an existing resource by id
        Uses posted data from Edit method

        """
        # create form instance from the ResourceModel
        entity_id = int(id)
        resource_model_form = model_form(ResourceModel)
        entity = ResourceModel.get_by_id(entity_id)
        form = resource_model_form(self.request.POST, obj=entity)

        context = {
            'id': id,
            'action': 'Update',
            'form': form,
            'submit_routename': 'resource.update'
        }

        # since this method is only called from a post,
        # we do not need to check for request.method == "POST"
        # if self.form.validate() returns true, then save
        # the data
        if form.validate():
            logging.debug('Form Validated!')
            # push form values into model
            form.populate_obj(entity)
            # save to data store
            key = entity.put()
            # redirect to index and/or edit form with new id
            logging.debug('key={0}'.format(key))
            # redirect to the edit page for the created id
            return webapp2.redirect_to('resource.edit', id=key.id())

        # the form did not validate, redisplay with errors
        return self.render_response('resource.html', context)

    def delete(self, id):
        """
        New method

        Delete an existing resource by id

        """
        context = {'action': 'Delete'}
        self.render_response('resource.html', context)
