from flask import Flask, request, jsonify, render_template
from model import generate_sql_query
from query_handler import fetch_from_db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  

@app.route("/ask", methods=["POST"])
def answer_query():
    data = request.get_json()
    user_query = data.get("query", "").strip()
    
    if not user_query:
        return jsonify({"error": "Query cannot be empty."}), 400
    
    sql_query = generate_sql_query(user_query)
    
    result = fetch_from_db(sql_query)
    
    return jsonify({"query": sql_query, "response": result})

if __name__ == "__main__":
    app.run(debug=True)
