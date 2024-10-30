from flask import Flask, render_template, request, send_file, flash
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
    error_message = None
    sql_query = request.form.get('sql', '')

    if request.method == 'POST':
        action = request.form['action']
        if action == 'Clear':
            return render_template('index.html', query_result=None, headers=None, query_history=QUERY_HISTORY, sql_query='')

        if not sql_query.strip():
            error_message = 'SQL query cannot be empty.'
        else:
            try:
                conn = sqlite3.connect(DATABASE)
                cursor = conn.cursor()
                # Split the SQL query into individual statements
                statements = sql_query.split(';')
                for statement in statements:
                    if statement.strip():
                        cursor.execute(statement)
                rows = cursor.fetchall()
                headers = [description[0] for description in cursor.description]
                conn.commit()
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
                error_message = f"An error occurred: {e}"

    return render_template('index.html', query_result=query_result, headers=headers, query_history=QUERY_HISTORY, error_message=error_message, sql_query=sql_query)

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
