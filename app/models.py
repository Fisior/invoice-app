class Customer(db.Model):
    id = db.Column(db.Integar, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    invoices = db.relationship('Invoice', backref='customer', lazy=True)
