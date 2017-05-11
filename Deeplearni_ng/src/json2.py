# Module declarations 
import json as j
"""
Description: Determine whether a key exists or not for the given example 
"""

# Global variables

# Functions
def isPalindrome(s):
	if isinstance(s,str) == False:
		A = str(s)
		return A == A[::-1]
	else:
		return s == s[::-1]

# This is for a tree of height 1
def key_value_pair_exist_top_level(key,dict1):
	try:
		if isPalindrome(dict1[key]):
			return True
	except KeyError:
			return False

# For a tree of height n
"""
Preconditions: Key to search for and a a data struct
Postconditions: An array of strings of every matched value 
"""
def key_value_pair_generator_recursive(key,dict1):
	dict_string_arr = []
	if isinstance(dict1, dict):
		for k, v in dict1.items():
			if k == key:
				# add to the dictionary
				dict_string_arr.append(v)
			else:
				if isinstance(v,list):
					for item in v:
						for k_c in key_value_pair_generator_recursive(key,item):
							dict_string_arr.append(k_c)
	return dict_string_arr

# For a tree of height n
"""
Preconditions: Key to search for and a a data struct
Postconditions: An array of strings that are palindromes
"""
def key_value_pair_all_palindromes_recursive(dict1):
	dict_string_arr = []
	if isinstance(dict1, dict):
		for k, v in dict1.items():
			if isPalindrome(v):
				# add to the dictionary
				dict_string_arr.append(v)
			else:
				if isinstance(v,list):
					for item in v:
						for k_c in key_value_pair_all_palindromes_recursive(item):
							dict_string_arr.append(k_c)
	return dict_string_arr
def file_to_dict(json_file):
	json1_str = json_file.read()
	try:
		json1_data = j.loads(json1_str)
		return json1_data
	except ValueError:
		print("JSON file is incorrectly formatted.")
	 	return
def count(word,dict1):
	c = 0
	for v in key_value_pair_generator_recursive(word,dict1):
		if isPalindrome(v):
			c+=1	
	return c	
def print_palindrome(word,dict1):
	B =[]
	for v in key_value_pair_generator_recursive(word,dict1):
		if isPalindrome(v):
			B.append(v)	
	return B

def count_all_palindromes(dict1):
	c = 0
	for v in key_value_pair_all_palindromes_recursive(dict1):
		c+=1	
	return c
