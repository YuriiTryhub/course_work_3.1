from flask import Flask, jsonify

from app.main.views import main_blueprint
from app.post.views import post_blueprint
from app.search.viewes import search_blueprint
from app.user_feed.viewes import user_feed_blueprint
from app_api.views import app_api
from logger import config 


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_feed_blueprint)
app.register_blueprint(app_api, url_prefix='/api')

config()

@app.errorhandler(404)
def page_error_404(error):
    return f'Такой страницы не существует {error}', 404

@app.errorhandler(500)
def page_error_500(error):
    return f'На сервере произошла ошибка {error}', 500

if __name__ == '__main__':
    app.run()