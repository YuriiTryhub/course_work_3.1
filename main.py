from flask import Flask, jsonify

from app.main.views import main_blueprint
from app.post.views import post_blueprint
from app.search.viewes import search_blueprint
from app.user_feed.viewes import user_feed_blueprint

from app.dao.main_dao import get_posts_all, get_post_by_pk


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_feed_blueprint)


@app.route('/api/posts')
def get_posts():
    posts = get_posts_all()
    return jsonify(posts)


@app.route('/api/posts/<int:post_id>')
def get_post_id(post_id):
    return get_post_by_pk(post_id)


if __name__ == '__main__':
    app.run()