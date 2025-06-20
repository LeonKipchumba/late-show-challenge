from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.app import db

episode_bp = Blueprint('episodes', __name__, url_prefix='/episodes')

@episode_bp.route('', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes]), 200

@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = Appearance.query.filter_by(episode_id=id).all()
    return jsonify({
        'episode': episode.to_dict(),
        'appearances': [a.to_dict() for a in appearances]
    }), 200

@episode_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'Episode deleted'}), 200
