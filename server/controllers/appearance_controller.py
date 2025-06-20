from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from server.app import db

appearance_bp = Blueprint('appearances', __name__, url_prefix='/appearances')

@appearance_bp.route('', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    guest_id = data.get('guest_id')
    episode_id = data.get('episode_id')
    if not (rating and guest_id and episode_id):
        return jsonify({'error': 'Missing fields'}), 400
    try:
        appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
