from flask import Blueprint, jsonify, request, abort
from .services import add_entry, get_entry, list_entries, delete_entry

bp = Blueprint('api', __name__)

@bp.route('/health', methods=['GET'])
def health():
    return jsonify({'status':'ok'})

@bp.route('/entries', methods=['GET','POST'])
def entries():
    if request.method == 'GET':
        ents = list_entries()
        return jsonify([e.__dict__ for e in ents])
    data = request.get_json()
    if not data:
        abort(400, 'JSON body required')
    required = ['user','activity','duration_minutes']
    for r in required:
        if r not in data:
            abort(400, f"missing field: {r}")
    e = add_entry(data['user'], data['activity'], data['duration_minutes'], data.get('category','general'))
    return jsonify(e.__dict__), 201

@bp.route('/entries/<entry_id>', methods=['GET','DELETE'])
def entry_detail(entry_id):
    e = get_entry(entry_id)
    if not e:
        abort(404)
    if request.method == 'GET':
        return jsonify(e.__dict__)
    delete_entry(entry_id)
    return '', 204
