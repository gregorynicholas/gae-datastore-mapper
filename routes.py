from webapp2_extras.routes import RedirectRoute
import logging

# Route Template
# RedirectRoute(template,
                # handler=None,
                # name=None,
                # defaults=None,
                # build_only=False,
                # handler_method=None,
                # methods=None,
                # schemes=None,
                # redirect_to=None,
                # redirect_to_name=None,
                # strict_slash=False)

secure_scheme = 'https'

_routes = [

    RedirectRoute('/generate_files/',
                  handler='handlers.file.FileHandler',
                  name='file.generate_files',
                  defaults=None,
                  handler_method='generate_files',
                  methods='GET',
                  schemes=None,
                  redirect_to=None,
                  redirect_to_name=None,
                  strict_slash=True),

    RedirectRoute('/count_files/',
                  handler='handlers.file.FileHandler',
                  name='file.count_files',
                  defaults=None,
                  handler_method='count_files',
                  methods='GET',
                  schemes=None,
                  redirect_to=None,
                  redirect_to_name=None,
                  strict_slash=True),

    RedirectRoute('/cleanup_files/',
                  handler='handlers.file.FileHandler',
                  name='file.cleanup_files',
                  defaults=None,
                  handler_method='cleanup_files',
                  methods='GET',
                  schemes=None,
                  redirect_to=None,
                  redirect_to_name=None,
                  strict_slash=True),

    # index of resources / collection of resources
    RedirectRoute('/resources/',
                  handler='handlers.resource.ResourceHandler',
                  name='resource.index',
                  defaults=None,
                  handler_method='index',
                  methods='GET',
                  schemes=None,
                  redirect_to=None,
                  redirect_to_name=None,
                  strict_slash=True),

    # display input to create a new resource
    # HTML Form Handler
    RedirectRoute('/resources/new/',
                  handler='handlers.resource.ResourceHandler',
                  name='resource.new',
                  defaults=None,
                  handler_method='new',
                  methods='GET',
                  schemes=None,
                  redirect_to=None,
                  redirect_to_name=None,
                  strict_slash=True),

    # display an existing resource
    RedirectRoute('/resources/<id>/',
                  handler='handlers.resource.ResourceHandler',
                  name='resource.show',
                  defaults=None,
                  handler_method='show',
                  methods='GET',
                  schemes=None,
                  redirect_to=None,
                  redirect_to_name=None,
                  strict_slash=True),

    # create a new resource via POST
    RedirectRoute('/resources/',
                  handler='handlers.resource.ResourceHandler',
                  name='resource.create',
                  defaults=None,
                  handler_method='create',
                  methods='POST',
                  schemes=None,
                  redirect_to=None,
                  redirect_to_name=None,
                  strict_slash=True),

    # edit an existing resource
    # HTML Form Handler
    RedirectRoute('/resources/<id>/edit/',
                  handler='handlers.resource.ResourceHandler',
                  name='resource.edit',
                  defaults=None,
                  handler_method='edit',
                  methods='GET',
                  schemes=None,
                  redirect_to=None,
                  redirect_to_name=None,
                  strict_slash=True),

    # POST/PUT updates to an existing resource
    # HTML Form Handler
    RedirectRoute('/resources/<id>/update/',
                  handler='handlers.resource.ResourceHandler',
                  name='resource.update',
                  defaults=None,
                  handler_method='update',
                  methods='POST',
                  schemes=None,
                  redirect_to=None,
                  redirect_to_name=None,
                  strict_slash=True),

    # PUT updates to an existing resource
    # RESTful API Handler
    RedirectRoute('/resources/<id>/',
                  handler='handlers.resource.ResourceHandler',
                  name='resource.update.api',
                  defaults=None,
                  handler_method='update',
                  methods='PUT',
                  schemes=None,
                  redirect_to=None,
                  redirect_to_name=None,
                  strict_slash=True),

    # POST /delete to delete an existing resource
    # HTML Form Handler
    RedirectRoute('/resources/<id>/delete/',
                  handler='handlers.resource.ResourceHandler',
                  name='resource.delete',
                  defaults=None,
                  handler_method='delete',
                  methods='POST',
                  schemes=None,
                  redirect_to=None,
                  redirect_to_name=None,
                  strict_slash=True),

    # DELETE an existing resource
    # RESTful API Handler
    RedirectRoute('/resources/<id>/',
                  handler='handlers.resource.ResourceHandler',
                  name='resource.delete.api',
                  defaults=None,
                  handler_method='delete',
                  methods='DELETE',
                  schemes=None,
                  redirect_to=None,
                  redirect_to_name=None,
                  strict_slash=True),


    # generic routes at the bottom
    RedirectRoute('/<template_name>/',
                  handler='handlers.template.TemplateHandler',
                  name='template-handler',
                  defaults=None,
                  handler_method='get',
                  methods='GET',
                  schemes=None,
                  redirect_to=None,
                  redirect_to_name=None,
                  strict_slash=True),

    RedirectRoute('/',
                  handler='handlers.main.MainHandler',
                  name='main-handler',
                  defaults=None,
                  handler_method='get',
                  methods='GET',
                  schemes=None,
                  redirect_to=None,
                  redirect_to_name=None,
                  strict_slash=True),

    RedirectRoute('/_ah/warmup',
                  redirect_to_name='main-handler'),

    RedirectRoute('/secure',
                  redirect_to_name='main-handler',
                  schemes=secure_scheme),

]


def get_routes():
    return _routes


def add_routes(app):
    secure_scheme = 'https'
    if app.debug:
        secure_scheme = 'http'
    logging.debug('secure_scheme={0}'.format(secure_scheme))
    for r in _routes:
        app.router.add(r)


    # Notes on route design
    # ---------------------
    # MVC
    # Controller/Action/id

    # webapp
    # GET/POST

    # Create
    # POST /participants/create
    # create_participant
    # POST /api/participants

    # Read
    # GET /participants/<id>
    # get_participant(id)
    # GET /api/participants/<id>

    # Update
    # POST /participants/<id>/update
    # update_participant(id)
    # PUT /api/participants/<id>

    # Delete
    # POST /participants/<id>/delete
    # delete_participant(id)
    # DELETE /api/participants/<id>

    ################################

    # REST
    # /resource/state/<id>
    # /user/profile/1
    # GET, POST, PUT, DELETE

    # Create
    # POST /participants

    # Read
    # GET /participants/<id>

    # Update
    # PUT /participants/<id>

    # Delete
    # DELETE /participants/<id>
