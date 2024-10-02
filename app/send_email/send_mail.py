from flask import Flask, render_template, request, flash, url_for, redirect, Blueprint

send_mail_bp = Blueprint('send_mail_bp', __name__)

@send_mail_bp.route('/write', methods=['GET', 'POST'])
def write_email():
    if request.method == 'POST':
        to_email = request.form['to_email']
        subject = request.form['subject']
        message_body = request.form['message_body']
        
        try:
            # Отправка письма через SMTP
            msg = MIMEText(message_body)
            msg['Subject'] = subject
            msg['From'] = app.config['EMAIL_ADDRESS']
            msg['To'] = to_email

            with smtplib.SMTP(app.config['SMTP_SERVER'], app.config['SMTP_PORT']) as server:
                server.starttls()
                server.login(app.config['EMAIL_ADDRESS'], app.config['EMAIL_PASSWORD'])
                server.sendmail(app.config['EMAIL_ADDRESS'], to_email, msg.as_string())

            flash('Email sent successfully!', 'success')
            return redirect(url_for('main.inbox'))
        except Exception as e:
            flash(f'Failed to send email: {str(e)}', 'danger')

    return render_template('write_email.html')