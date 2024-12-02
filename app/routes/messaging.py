from flask import Blueprint, request, jsonify
from ..models.recipients import Recipient
from ..models.bot import send_message

messagingBp = Blueprint('messaging', __name__)

@messagingBp.route('/send_message', methods=['POST'])
async def add_recipient():
    data = request.get_json()
    message = data.get('message')
    conversation_id = data.get('conversation_id')
    recipients = []

    if message is None:
        return jsonify({"message": "Missing message"}), 400

    if conversation_id:
        recipients = [Recipient.query.filter_by(conversation_id=conversation_id).first()]
    else:
        recipients = Recipient.query.all()
    
    for recipient in recipients:
        await send_message(message, recipient.conversation_id)

    return jsonify({"message": "Message sent"}), 200