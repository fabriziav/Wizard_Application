from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# VULNERABILITY: Embedded third-party API key
STRIPE_API_KEY = "sk_live_51Habcdefghijklmnopqrstuvwxyz123456789"

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # VULNERABILITY: SQL Injection (using string formatting instead of parameterized queries)
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return str(cursor.fetchall())

@app.route('/ping')
def ping_host():
    host = request.args.get('host')

    # VULNERABILITY: Command Injection (passing unsanitized user input directly to the OS shell)
    command = f"ping -c 1 {host}"
    result = os.popen(command).read()
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # test comment

