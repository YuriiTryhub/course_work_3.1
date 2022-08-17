from flask import Blueprint, jsonify

from app.dao.main_dao import get_posts_all, get_post_by_pk

app_api = Blueprint('app_api', __name__)


@app_api.route('/')
def app_posts_hi():

    return 'Hello in API ;P Эндпоинты api/posts, api/post/<post_id>'

@app_api.route('/posts/')
def app_posts_all():
    posts = get_posts_all()
    return jsonify(posts)


@app_api.route('/post/<int:post_id>/')
def app_posts_single(post_id: int):
    post_pk = get_post_by_pk(post_id)
    return jsonify(post_pk)


@app_api.errorhandler(404)
def app_error_404(error):
    return jsonify({'error': str(error)}), 404