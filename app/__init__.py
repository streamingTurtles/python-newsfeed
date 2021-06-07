from app.routes import home, dashboard
from flask import Flask
from app.db import init_db
# _x - to use your custom filter functions, they need to be registered with the Jinja template environment - here
# and add code to the create_app() function
from app.utils import filters




def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )
  # _x - with this registration, we can now use these functions after add the filters to the template files
  # updating the following 3 .html templates - post-info.html, comments.html & edit-post.html
  # _x - now we need to update the span in the template for post-info located at - app/templates/partials/post-info.html
  app.jinja_env.filters['format_url'] = filters.format_url
  app.jinja_env.filters['format_date'] = filters.format_date
  app.jinja_env.filters['format_plural'] = filters.format_plural
  



  @app.route('/hello')
  def hello():
    return 'hello world'





  # register routes 
  app.register_blueprint(home) 
  app.register_blueprint(dashboard)
  # init_db()
  init_db(app)
  return app