import config
from flask import Flask

app = Flask(__name__)
app.config.from_object(config.config_environments['development'])
app.config['SECRET_KEY'] = "allan2327,."
