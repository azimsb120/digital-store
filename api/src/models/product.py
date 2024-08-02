from ..db import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    creator = db.relationship("User", backref=db.backref("products", lazy=True))

    def __repr__(self):
        return f"<Product {self.name}>"
