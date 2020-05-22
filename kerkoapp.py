from flask import Flask
from kerko.composer import Composer
from flask_babelex import Babel
from flask_bootstrap import Bootstrap
from kerko import blueprint as kerko_blueprint


app = Flask(__name__)
app.config['SECRET_KEY'] = 'K#d{c^#KgD=s.Kq'  # Replace this value.
app.config['KERKO_ZOTERO_API_KEY'] = 'DUTwl21GgxVc74bGODObxDut'  # Replace this value.
app.config['KERKO_ZOTERO_LIBRARY_ID'] = '5778088'  # Replace this value.
app.config['KERKO_ZOTERO_LIBRARY_TYPE'] = 'user'  # Replace this value if necessary.
app.config['KERKO_COMPOSER'] = Composer()

babel = Babel(app)
bootstrap = Bootstrap(app)
app.register_blueprint(kerko_blueprint, url_prefix='/bibliography')