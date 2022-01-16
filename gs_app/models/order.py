from gs_app import db
from .cart import Cart


class Order(db.Document):
    cart = db.ReferenceField(Cart)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField(required=True)
    phone = db.StringField(required=True)
    payment_type = db.StringField(required=True)
    comment = db.StringField(max_lenght=600)

    def to_dict(self):
        return {
            '_id': str(self.pk),
            'first_name': self.firstname,
            'last_name': self.lastname,
            'email': self.email,
            'phone': self.phone,
            'payment_type': self.payment_type,
            'comment': self.comment
        }
