from flask import Flask,render_template,request,redirect,url_for
from database import fetch_data,insert_products,insert_sales,insert_stock
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
    products=fetch_data('products')
    Mys=fetch_data('sales')
    # print(Mys)
    return render_template('sales.html',my_sales=Mys,products=products)
#add sales

@app.route('/add_sales',methods=['GET','POST'])
def add_sales():
    if request.method=='POST':
        prod_id=request.form['pid']
        pq=request.form['Pquantity']
        new_sales=(prod_id,pq)
        insert_sales(new_sales)
        return redirect(url_for('sales'))
    return redirect(url_for('sales'))




#stock route
@app.route('/stock')
def stock():
    Mysto=fetch_data('stock')
    # print(Mysto)
    return render_template('stock.html',my_stock=Mysto)
 #add stock
@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method=='POST':
        stock=request.form['pid']
        sq=request.form['squantity']
        new_stock=(stock,sq)
        insert_stock(new_stock)
        return redirect(url_for('stock'))
    return redirect(url_for('stock'))

app.run(debug=True)
