from .. import db

class Recipient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    conversation_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Recipient {self.name}, Conversation {self.conversation_id}>"
