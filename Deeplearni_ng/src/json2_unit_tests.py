# Module declarations
import json2 as j

# Unit tests ...

"""
Description: In this case we expect a true the method to return true
"""

# Global variables
file_path = "../json_object/json_file.JSON"

# Functions
def unit_test_height_1(key,file_path):
	with open(file_path) as json_file:
		dict1 = j.file_to_dict(json_file)
		if j.key_value_pair_exist_top_level(key,dict1) == False:
			return False
		else:
			return True

def unit_test_palindrome(arg):
	return j.isPalindrome(arg) 

# Main Python unit test code
key_1 = "word"
key_2 = "key"
key_3 = "jo"

# Running all unit tests for height = 1
Result = []
final_result = True
with open(file_path) as json_file:
	dict1 = j.file_to_dict(json_file)
	if unit_test_height_1(key_1,file_path) == True:
		Result.append(True)
	else: 
		Result.append(False)

	if unit_test_height_1(key_2,file_path) == True:
		Result.append(True)
	else:
		Result.append(False)
	if unit_test_height_1(key_3,file_path) == False:
		Result.append(True)
	else:
		Result.append(False)

str_t1 = 'jjj'
str_t2 = 'not_p'

if unit_test_palindrome(str_t1) == True:
	Result.append(True)
else:
	Result.append(False)
if unit_test_palindrome(str_t2) == False:
	Result.append(True)
else:
	Result.append(False)

	for v in Result:
		final_result = final_result and v
	if final_result == False:
		print("Some unit tests may have failed")
