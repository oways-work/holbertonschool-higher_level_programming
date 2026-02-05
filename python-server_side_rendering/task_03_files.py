from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    data = []
    error = None

    if source == 'json':
        try:
            data = read_json()
        except FileNotFoundError:
            error = "Data not found"
    elif source == 'csv':
        try:
            data = read_csv()
        except FileNotFoundError:
            error = "Data not found"
    else:
        error = "Wrong source"

    if not error and product_id:
        data = [p for p in data if p['id'] == product_id]
        if not data:
            error = "Product not found"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
