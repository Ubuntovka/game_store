from gs_app import db


class Order(db.Document):
    firstname = db.StringField(required=True)
    lastname = db.StringField(required=True)
    email = db.EmailField(required=True)
    phone = db.StringField(required=True)
    payment_type = db.StringField(required=True)
    comment = db.StringField(max_lenght=600)

    def to_dict(self):
        return {
            '_id': str(self.pk),
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'phone': self.phone,
            'payment_type': self.payment_type,
            'comment': self.comment
        }
