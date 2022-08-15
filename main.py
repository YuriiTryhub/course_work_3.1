from flask import Flask, jsonify
from app.main.views import main_blueprint

from app.dao.main_dao import get_posts_all, get_post_by_pk


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run()