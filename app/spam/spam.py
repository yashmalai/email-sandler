from flask import Blueprint, render_template
from app.utils import get_emails

spam_bp = Blueprint('spam_bp', __name__)

@spam_bp.route('/')
def spam():
    emails = get_emails('Spam')
    return render_template('spam.html', emails=emails)