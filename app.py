from flask import Flask, request, jsonify
from limiter import Limiter


app = Flask(__name__)

limiter = Limiter()

@app.route('/limit', methods=['GET']) # example route
def limit():
    ip_address = request.remote_addr  # Get client IP
    user_id = request.headers.get('user_id', 'anonymous') # default to anonymous if user_id is not provided

    key_user = f'user:{user_id}' # to be used when we want to limit based on user_id
    key_ip = f'ip:{ip_address}' # to be used when we want to limit based on IP address
    
    if limiter.limit(key_ip):
        return jsonify({'message': 'Request accepted',
                        'ip_address': ip_address})
    else:
        return jsonify({'message': 'Request rejected',
                        'ip_address': ip_address}), 429

if __name__ == '__main__':
    app.run(debug=True)
