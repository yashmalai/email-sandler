from app.inbox import inbox_bp
from app.spam import spam_bp


def bp_register(app):
    app.register_blueprint(inbox_bp, url_prefix = '/')
    app.register_blueprint(spam_bp, url_prefix = '/spam')

    pass