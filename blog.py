# -*- coding: utf-8 -*-
from bottle import Bottle, debug, static_file
from bottle import cheetah_template
import articles
import os

app = Bottle()


def template_layout(template, *args, **kwargs):
    layout_yield = cheetah_template(template, args, kwargs)
    kwargs_more = dict(kwargs.items() + {"layout_yield": layout_yield,
                                         "articles": loader.get_all_articles()}.items())

    return cheetah_template("layout", *args, **kwargs_more)


@app.route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./static')


@app.route('/<slug>')
def article(slug):
    """the page for a single article"""
    article = loader.get_article(slug)
    return template_layout("article", article=article)


@app.route('/')
def index():
    """the index page"""
    arts = loader.get_all_articles()
    print(arts.keys())
    return template_layout("index", articles=arts)


@app.route('/contact')
def contact():
    """contact me page"""
    return "cool"

if __name__ == "__main__":
    loader = articles.Loader()
    debug(True)
    app.run(server='gunicorn', host="0.0.0.0", port=os.environ.get('PORT', 5000), reloader=True)
