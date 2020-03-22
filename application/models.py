from application import db
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prayer_type = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    callingTime = db.Column(db.String(100), nullable=False, unique=True)
    prayingTime = db.Column(db.String(500), nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'Prayer: ', self.prayer_type, ' ', self.city, '\r\n',
            'Calling: ', self.callingTime, '\r\n', self.prayingTime
            ])