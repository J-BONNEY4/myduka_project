import psycopg2
connect=psycopg2.connect(
    host='localhost',
    user='postgres',
    dbname='myduka_db',
    port=5432,
    password='Mutui044@'
)
#declare cursor to perform db operations
cur=connect.cursor()
#db operations
# cur.execute('select * from products;')
# products=cur.fetchall()
# print(products)
# def fetch_products():
#     cur.execute('select * from products;')
#     products=cur.fetchall()
#     return products
# myProducts=fetch_products()
# print('products')
# print(myProducts)

# def fetch_sales():
#     cur.execute('select * from sales;')
#     sales=cur.fetchall()
#     return sales
# mySales=fetch_sales()
# print('sales')
# print(mySales)
# def fetch_stock():
#      cur.execute('select * from stock;')
#      stock=cur.fetchall()
#      return stock
# myStock=fetch_stock()
# print('stock')
# print(myStock)
# # cur.execute('select * from sales;')
# # sales=cur.fetchall()
# # print(sales)
# # cur.execute('select * from stock;')
# # stock=cur.fetchall()
# # print(stock)
# cur.execute("insert into products(name,buying_price,selling_price)values('bread',40,60);")
# connect.commit()
# cur.execute("insert into products(name,buying_price,selling_price)values('Rice',100,160);")
# connect.commit()
# cur.execute("insert into products(name,buying_price,selling_price)values('Tea leaves',35,75);")
# connect.commit()
# cur.execute("insert into stock (product_id, stock_quantity) VALUES (4, 170);")
# connect.commit()
# cur.execute("insert into sales (product_id,quantity) VALUES (4, 90);")
# connect.commit()

# fetch data
def fetch_data(table_name):
    cur.execute(f'select * from {table_name}')
    data=cur.fetchall()
    return data
# products=fetch_data('products')
# print(products)
# sales=fetch_data('sales')
# print(sales)
# stock=fetch_data('stock')
# print(stock)


#insert products
def insert_products(values):
    query="insert into products(name,buying_price,selling_price)values(%s,%s,%s);"
    cur.execute(query,values)
    connect.commit()
# new_product=('Oranges',15,25)
# # insert_products(new_product)
# products=fetch_data('products')
# print(products)

#insert sales
def insert_sales(values):
    query="insert into sales(product_id,quantity,created_at)values(%s,%s,now());"
    cur.execute(query,values)
    connect.commit()
# new_sale=(6,25)
# # insert_sales(new_sale)
# sales=fetch_data('sales')
# print(sales)
#insert stock
def insert_stock(values):
    query="insert into stock(product_id,stock_quantity)values(%s,%s);"
    cur.execute(query,values)
    connect.commit()
# new_stock=(7,40)
# # insert_stock(new_stock)
# stock=fetch_data('stock')
# print(stock)

#1.Query to get profit per product
def product_profit():
    query='select p.name,p.id, sum((p.selling_price-p.buying_price)*s.quantity) as total_profit from products as p join ' \
    'sales as s on p.id=s.product_id group by p.name,p.id;'
    cur.execute(query)
    profit=cur.fetchall()
    return profit
# my_profit=product_profit
# print('profit')
# print(my_profit)

#2.Query to get sales per product
def product_sale():
    query='select p.name,p.id, sum(p.selling_price*s.quantity) as total_profit from products as p join ' \
    'sales as s on p.id=s.product_id group by p.name,p.id;'
    cur.execute(query)
    sales=cur.fetchall()
    return sales
# my_sales=product_sale()
# print('sales')
# print(my_sales)
