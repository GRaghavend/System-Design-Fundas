from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def get_data():
    conn = sqlite3.connect("database.db")
    
    cursor = conn.cursor()
    
    print("Connected to the database successfully.")
    
    cursor.execute("SELECT Letters FROM letters LIMIT 1")
    
    result = cursor.fetchone()
    
    print(f"Fetched letter from database: {result[0] if result else 'No data found'}")
    
    conn.close()
    
    return jsonify(
        {"letter": result[0] if result else None}
    )
    
if __name__ == "__main__":
    app.run(debug=True)