from flask import Flask, render_template, jsonify, request, send_from_directory
import sqlite3

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')


@app.route('/fetch_results', methods=['POST'])
def fetch_results():
    byzantine_value = request.form.get('byzantineValue')
    
    # Construct the database filename and table name based on the byzantine value
    db_name = f"results_byzcount_{byzantine_value}.db"
    table_name = f"results_byzcount_{byzantine_value}"
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Query to fetch data based on the byzantine value
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    conn.close()
    
    # Convert rows to dictionary format for easy JSON serialization
    results = []
    for row in rows:
        result_dict = {
            'gar': row[0],
            'best_accuracy': row[1],
            'worst_best_accuracy': row[2],
            # Add other fields here as per your table columns
        }
        results.append(result_dict)
    
    return jsonify(results)



if __name__ == '__main__':
    app.run(debug=True)
