from app import app
from flask import render_template
from models.list_of_orders import orders

@app.route('/orders')
def get_orders():
    return render_template('index.html', title="Home Page", orders=orders)

@app.route('/orders/<index>')
def view_order(index):
    return render_template('order.html', order=orders[int(index)])
