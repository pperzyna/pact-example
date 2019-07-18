
from flask import Flask, jsonify, make_response, abort, request

app = Flask(__name__, static_url_path = "")

users = [
    {
        'id': 1,
        'name': u'Monty Python',
        'description': u'British surreal comedy group', 
        'active': False
    },
    {
        'id': 2,
        'name': u'Johnnie Walker',
        'description': u'Brand of Scotch whisky', 
        'active': True
    }
]

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/user', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/user/<int:user_id>', methods = ['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify(user[0])

@app.route('/user/<int:user_id>', methods=['DELETE'])    
def del_user(user_id):
    user = [users.index(user) for user in users if user['id'] == int(user_id)]
    if len(user) == 0:
        abort(404)
    del users[user[0]]
    return make_response(jsonify( { 'response': 'User has been removed' } ), 200)

@app.route('/user', methods=['POST'])
def post_user():
    if not request.json or not 'name' in request.json:
        abort(400)
    user = add_user(users[-1]['id'] + 1 ,request.json['name'], request.json.get('description', ""))
    return jsonify(user), 201

def add_user(user_id, user_name, user_description=''):
    user = {
        'id': int(user_id),
        'name': user_name,
        'description': user_description,
        'active': True
    }
    users.append(user)
    return user
    
@app.route('/_pact/provider_state', methods=['POST'])
def provider_states():
    if request.json['state'] == "User with id 3 exists":
        add_user(3, "Test")
    if request.json['state'] == "User with id 1 does not exist":
        del_user(1)

    return make_response(jsonify( { 'response': 'State has been applied' } ), 200)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)