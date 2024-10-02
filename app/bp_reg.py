from app.inbox import inbox_bp
from app.spam import spam_bp
from app.send_email import send_mail_bp


def bp_register(app):
    app.register_blueprint(inbox_bp, url_prefix = '/')
    app.register_blueprint(spam_bp, url_prefix = '/spam')
    app.register_blueprint(send_mail_bp, url_prefix = '/send')
    pass