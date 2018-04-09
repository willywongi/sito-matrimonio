import os
import sys

from flask import Flask, send_file
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/')
def index():
	return send_file(os.path.join('..', 'src', 'index.html'), mimetype='text/html')

@app.route('/istruzioni')
def index():
	return send_file(os.path.join('..', 'src', 'lista_aiuto.html'), mimetype='text/html')


if __name__ == "__main__":
	try:
		port = int(sys.argv[1])
	except IndexError:
		port = 5000
	app.run(host='0.0.0.0', port=port, debug=True)