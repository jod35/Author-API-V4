from flask import Flask
from .config import DevConfig
from src.utils.database import db
from src.models.authors import Author

app=Flask(__name__)

app.config.from_object(DevConfig)

db.init_app(app)


@app.shell_context_processor
def make_shell_context():
    return {
        'app':app,
        'db':db,
        'author_model':Author
    }


