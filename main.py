from flask import Flask,render_template
from database import fetch_data
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

# products route
@app.route('/products')
def products():
    prods=fetch_data('products')
    # print(prods)
    return render_template('products.html',my_products=prods)


#sales route
@app.route('/sales')
def sales():
    Mys=fetch_data('sales')
    # print(Mys)
    return render_template('sales.html',My_sales=Mys)

#stock route
@app.route('/stock')
def stock():
    Mysto=fetch_data('stock')
    # print(Mysto)
    return render_template('stock.html',my_stock=Mysto)
app.run()
