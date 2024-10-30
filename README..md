# SQL to CSV Exporter

This is a simple web-based application built with Flask that allows users to input SQL queries, execute them against a SQLite database, and export the results to a CSV file.

## Features

- Execute SQL queries on a SQLite database.
- Export query results to a CSV file.
- User-friendly interface with error handling and feedback.

## Project Structure


## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd your_app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

- Enter your SQL query in the provided textarea.
- Click the "Execute and Export" button to run the query.
- If successful, the results will be downloaded as a CSV file.

## Notes

- **Security**: This application executes raw SQL queries, which can be dangerous if exposed to untrusted users. Ensure that this application is used in a secure, controlled environment.
- **Database Setup**: The application initializes with a sample SQLite database (`database.db`). You can customize this database with your own tables and data as needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/).