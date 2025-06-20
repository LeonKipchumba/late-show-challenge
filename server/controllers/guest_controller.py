from flask import Blueprint, jsonify
from server.models.guest import Guest
from server.app import db

guest_bp = Blueprint('guests', __name__, url_prefix='/guests')

@guest_bp.route('', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests]), 200
