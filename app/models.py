from app import db

class Customer(db.Model):
    id = db.Column(db.Integar, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    invoices = db.relationship('Invoice', backref='customer', lazy=True)


class Invoice(db.Model):
    id = db.Column(db.Integar, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Data, nullable=False)
    customer_id = db.Column(db.Integar, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship('Customer', backref=db.backref('invoices'), lazy=True)
