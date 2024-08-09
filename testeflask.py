from flask import Flask, jsonify
from SqlServerQueries import NfeQuery

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    obj = NfeQuery()
    obj.autentication_database()
    data = obj.execute_sql_query()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)