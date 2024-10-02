from flask import Flask, render_template, request, flash, url_for, redirect, Blueprint
from app.utils import send_email

send_mail_bp = Blueprint('send_mail_bp', __name__)

@send_mail_bp.route('/')
def menu():
    return render_template('sendmail.html')

@send_mail_bp.route('/', methods=['POST'])
def write_email():
    to_email = request.form['to_email']
    subject = request.form['subject']
    message_body = request.form['message_body']
    
    try:
        send_email(message_body, subject, to_email)
        flash('Email sent successfully!', 'success')
        return redirect(url_for('inbox_bp.inbox'))
    except Exception as e:
        flash(f'Failed to send email: {str(e)}', 'danger')

    