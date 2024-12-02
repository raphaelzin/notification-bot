from flask import Blueprint, request, jsonify
from ..models.recipients import db, Recipient

bp = Blueprint('routes', __name__)

@bp.route('/add_recipient', methods=['POST'])
def add_recipient():
    data = request.get_json()
    name = data.get('name')
    conversation_id = data.get('conversation_id')

    new_recipient = Recipient(name=name, conversation_id=conversation_id)
    db.session.add(new_recipient)
    db.session.commit()

    return jsonify({"message": "Recipient added"}), 201

@bp.route('/recipients', methods=['GET'])
def get_recipients():
    recipients = Recipient.query.all()
    return jsonify([{"id": recipient.id, "name": recipient.name, "conversation_id": recipient.conversation_id} for recipient in recipients])
