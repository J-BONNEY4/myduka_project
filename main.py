from flask import Flask,render_template,request,redirect,url_for
from database import fetch_data,insert_products
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

#add products.
@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method=='POST':
        pname=request.form['name']
        sp=request.form['Selling_Price']
        bp=request.form['Buying_Price']
        new_products=(pname,bp,sp)
        insert_products(new_products)
        return redirect(url_for('products'))
    return redirect(url_for('products'))



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


app.run(debug=True)
