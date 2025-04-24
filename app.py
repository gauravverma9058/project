from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="Sam@2003",  # Replace with your MySQL password
        database="phishing_detection"
    )

# Function to check URL
def check_url(url):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check in blacklisted URLs
    cursor.execute('SELECT * FROM blacklisted_urls WHERE url = %s', (url,))
    if cursor.fetchone():
        conn.close()
        return "Warning: It's a phishing URL"

    # Check in safe URLs
    cursor.execute('SELECT * FROM safe_urls WHERE url = %s', (url,))
    if cursor.fetchone():
        conn.close()
        return "The URL is safe"

    conn.close()
    return "The URL is not in the database. Analyze its syntax or proceed with caution."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    result = check_url(url)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)