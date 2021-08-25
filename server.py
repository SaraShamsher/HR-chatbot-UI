from flask import Flask, jsonify, request
from flask_cors import CORS
# import trainer
app = Flask(__name__)
CORS(app,support_credentials=True)

@app.route('/api/talk',methods=['POST'])
def index():
    user_input = request.form['user_input']
    return jsonify({'msg':'hello'})

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=10533, debug=True)
 