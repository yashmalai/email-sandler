from flask import Blueprint, render_template
from app.utils import get_emails

inbox_bp = Blueprint('inbox_bp', __name__)

@inbox_bp.route('/')
def inbox():
    emails = get_emails('INBOX')
    return render_template('inbox.html', emails=emails)