from flask import Blueprint, jsonify
from db import get_db_connection

emails_bp = Blueprint('emails', __name__)

@emails_bp.route('/api/emails', methods=['GET'])
def get_emails():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM RawEmails ORDER BY email_date DESC')
    emails = cursor.fetchall()

    cursor.close()
    connection.close()

    response = jsonify(emails)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
