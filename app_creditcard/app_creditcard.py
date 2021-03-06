import os
from flask import Flask, request, render_template, jsonify
from creditcard import CreditCard
from file import File

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
  assert request.path == '/validate'
  assert request.method == 'POST'

  print request.form['creditcard']
  cr = CreditCard(request.form['creditcard'])

  if(cr.validate()):
    return jsonify({'creditcard': cr.get_number(), 'valid': True})
  else:
    return jsonify({'creditcard': cr.get_number(), 'valid': False})

@app.route('/validate_file', methods=['POST'])
def validate_file():
  assert request.path == '/validate_file'
  assert request.method == 'POST'
  file = request.files['file']
  new_file = File(file)
  if(new_file.upload()):
    result = new_file.validate_credit_cards() 
    return jsonify(result)
  else:
    return jsonify({'error': 'File Upload failed.'})