#!../flask/bin/python

# module declarations

from flask import Flask, jsonify, request,render_template 
import json2 as j
from pprint import pprint
import sys

# Global Vars
app = Flask(__name__, template_folder='.')
file_path = sys.argv[-1] 
json_file = open(file_path)
json_dict  = j.file_to_dict(json_file)

if file_path == "./main.py":
	print("No file was provided.")
	raise ValueError('Missing file')
 
# Routes
@app.route('/',methods=['GET'])
def init():
    return jsonify({'Message':"REST API for Deeplearni.ng"})

@app.route('/palindromes/count',methods=['GET'])
def palindromes_count():
	# Get the count
	Count = j.count_all_palindromes(json_dict)
	return jsonify({"Palindrome_Count": str(Count)})

@app.route('/palindromes',methods=['GET'])
def palindromes():
	# return a string array of all palindromes
	A = j.key_value_pair_all_palindromes_recursive(json_dict)
	return render_template('template.html',your_list=A)

if __name__ == '__main__':
    app.run(debug=True)
