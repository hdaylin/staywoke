
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/dhenry9412/sites/staywoke/tmp/database.db'
db = SQLAlchemy(app)

class Art(db.Model):
    _tablename__= "Art"
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(20))
    description= db.Column(db.String)
    image = db.Column(db.String)

class Food(db.Model):
    _tablename__= "Food"
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(20))
    recipe_name= db.Column(db.String)
    recipe= db.Column(db.String)
    image = db.Column(db.String)

class Customer(db.Model):
    _tablename__= "Customer"
    id = db.Column(db.Integer, primary_key=True)
    cus_name = db.Column(db.String(20))
    cus_email = db.Column(db.String)
    cus_balance= db.Column(db.Float(2))

class Orders(db.Model):
    _tablename__= "Orders"
    id = db.Column(db.Integer, primary_key=True)
    cus_id = db.Column(db.Integer, db.ForeignKey('Customer.id'))
    cus_id = relationship("Customer", foreign_keys=[cus_id])
    order_date= db.Column(db.Date)
    order_balance= db.Column(db.Float)
    image = db.Column(db.String)


class Acct_transaction(db.Model):
    _tablename__= "Acct_transaction"
    id = db.Column(db.Integer, primary_key=True)
    cus_id = db.Column(db.Integer, db.ForeignKey('Customer.id'))
    cus_id = relationship("Customer", foreign_keys=[cus_id])
    trans_date = db.Column(db.Date)
    trans_amount= db.Column(db.Float)

class Product(db.Model):
    _tablename__= "Product"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('Orders.id'))
    order_id = relationship("Orders", foreign_keys=[order_id])
    prod_name = db.Column(db.String)
    price = db.Column(db.Float)

class Line(db.Model):
    _tablename__= "Line"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer,  db.ForeignKey('Orders.id'), primary_key=True)
    order_id = relationship("Orders", foreign_keys=[order_id])
    prod_id = db.Column(db.Integer, db.ForeignKey('Product.id'))
    prod_id = relationship("Product", foreign_keys=[prod_id])
    line_unit = db.Column(db.Integer)
    line_price = db.Column(db.Float)
    line_amount = db.Column(db.Float)



@app.route('/')

def index():
    return render_template('index.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route('/art')
def art():
    return render_template('art.html')

@app.route('/activism')
def activism():
    return render_template('activism.html')

@app.route('/food')
def food():
    return render_template('food.html')
@app.route('/love')
def love():
    return render_template('love.html')



