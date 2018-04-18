#!/usr/bin/env python3
from ManageProxy import ManageProxy
from flask import Flask, jsonify

app = Flask(__name__)

help = {
	'get_one' : 'get one valid proxy',
	'get_all' : 'get all proxy'
}

@app.route('/')
def index():
	return jsonify(help)

@app.route('/get_one/')
def get_one():
	obj = ManageProxy()
	return jsonify(obj.getRandomValidProxy())
	
@app.route('/get_all/')
def get_all():
	obj = ManageProxy()
	return jsonify(obj.getAllProxy())
	
def run():
	app.run(host='127.0.0.1', port=5050)

if __name__ == '__main__':
	run()