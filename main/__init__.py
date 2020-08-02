from flask import Flask
from .config import DevConfig
from main.utils.database import db



app=Flask(__name__)

app.config.from_object(DevConfig)
db.init_app(app)

from main.api.views import api_blueprint
app.register_blueprint(api_blueprint,url_prefix='/api')


from main.models.authors import Author
@app.shell_context_processor
def make_shell_context():
    return {
        'app':app,
        'db':db,
        'Author':Author
    }


