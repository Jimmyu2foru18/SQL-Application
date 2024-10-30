from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import sqlite3
import csv
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key
DATABASE = 'database.db'
CSV_FILE = 'output.csv'
QUERY_HISTORY = []

@app.route('/', methods=['GET', 'POST'])
def index():
    query_result = None
    headers = None
    if request.method == 'POST':
        sql_query = request.form['sql']
        if not sql_query.strip():
            flash('SQL query cannot be empty.', 'error')
            return redirect(url_for('index'))
        
        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.execute(sql_query)
            rows = cursor.fetchall()
            headers = [description[0] for description in cursor.description]
            conn.close()

            # Save query to history
            QUERY_HISTORY.append(sql_query)

            # Write to CSV
            with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(rows)

            query_result = rows
        except sqlite3.Error as e:
            flash(f"An error occurred: {e}", 'error')
            return redirect(url_for('index'))
    return render_template('index.html', query_result=query_result, headers=headers, query_history=QUERY_HISTORY)

if __name__ == '__main__':
    # Ensure the database exists
    if not os.path.exists(DATABASE):
        # Initialize with an example table
        conn = sqlite3.connect(DATABASE)
        conn.execute('''
            CREATE TABLE example (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')
        conn.executemany('INSERT INTO example (name, age) VALUES (?, ?)', [
            ('Alice', 30),
            ('Bob', 25),
            ('Charlie', 35)
        ])
        conn.commit()
        conn.close()
    app.run(debug=True)
