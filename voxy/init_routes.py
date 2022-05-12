"""
File to declare routes
"""


def init_routes(app):
    from voxy.wordcounting import wordcounting_bp
    app.register_blueprint(wordcounting_bp, url_prefix='/api/wordcounting')
