from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def get_json_data():
    with open('products.json', 'r') as f:
        return json.load(f)

def get_csv_data():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def get_sql_data():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    data = []
    error = None

    if source == 'json':
        data = get_json_data()
    elif source == 'csv':
        data = get_csv_data()
    elif source == 'sql':
        try:
            data = get_sql_data()
        except sqlite3.Error:
            error = "Database error"
    else:
        error = "Wrong source"

    if not error and product_id:
        data = [p for p in data if p['id'] == product_id]
        if not data:
            error = "Product not found"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
