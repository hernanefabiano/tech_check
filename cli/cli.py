'''
functions that accepts string representation of json data that includes arrays and rotate as keys.
'''

import json

class InvalidArgument(Exception):
	pass

def parse_args(arguments):
	arguments = json.loads(arguments)
	array_of_numbers, rotation = arguments.get("arrays"), arguments.get("rotate")
	return array_of_numbers, rotation

def missing_int(arguments):
	'''A. Given an array A of N integers, write a function missing_int(A) that 
       returns the smallest positive integer (greater than 0) that does not occur in A.
        ● A = [1, 3, 6, 4, 1, 2] should return 5
        ● A = [1, 2, 3] should return 4 ---> why should the return be 4?
        ● A = [-1, -1, -1, -5] should return 1
        ● A = [1, 3, 6, 4, 1, 7, 8, 10] should return 2
    '''
	array_of_numbers, _ = parse_args(arguments)
	print("array_of_numbers: ", array_of_numbers)
	
def find_divisible(arguments):
	'''Write a function find_divisible(a, b, k) that accepts three integers: a, b and k, 
       and returns the total count of the numbers between a and b (inclusive) 
	   that are divisible by k
        ● find_divisible(6,11,2) should return 3. 6, 8, and 10 are all divisible by 2.
        ● find_divisible(0,12,3) should return 5. 0, 3,6, 9, and 12 are all divisible by 3.
	'''
	new_arrays = []
	array_of_numbers, _ = parse_args(arguments)
	if len(array_of_numbers) < 3:
		raise InvalidArgument(
			f"find_divisible function expect 3 arguments, received {len(array_of_numbers)}"
			)
	
	left, right, divisible_by = array_of_numbers
	print(f"Input numbers: {array_of_numbers} ")
	new_arrays = [num for num in range(left, right) if not num % divisible_by]
	print(f"List of divisible Numbers({new_arrays}) by: {divisible_by}")


def rotate(arguments):
	'''Write a rotate(A, k) function which returns a rotated array A, k times; 
       that is, each element of A will be shifted to the right k times
        ● rotate([3, 8, 9, 7, 6], 3) returns [9, 7, 6, 3, 8]
        ● rotate([0, 0, 0], 1) returns [0, 0, 0]
        ● rotate([1, 2, 3, 4], 4) returns [1, 2, 3, 4]
	'''
	array_of_numbers, rotation = parse_args(arguments)
	if not all([array_of_numbers, rotation]):
		raise InvalidArgument(
			f"Invalid parameter, please check key:values arrays({array_of_numbers}), rotation({rotation})"
			)
	print(f"Input List: {array_of_numbers}")
	rotated_list = []
	for index, num in enumerate(array_of_numbers):
		print(f"rotating {num}...")
		rotated_list.append(
			array_of_numbers[(index - rotation) % len(array_of_numbers)]
			)
	print(f"Rotated numbers from left to right ({rotation})x: {rotated_list}")


def funct_controller(command, arguments):
    classification = {
        "missing" : "missing_int",
		"find" : "find_divisible",
        "rotate": "rotate",
    }
    return globals()[classification[command]](arguments)


def process_command(arguments):
	return funct_controller(
		arguments.command, arguments.argument
		)

	
if __name__ == "__main__":
	import argparse
	import textwrap

	parser = argparse.ArgumentParser(
		prog='cli', 
		formatter_class=argparse.RawDescriptionHelpFormatter, 
		epilog=textwrap.dedent('''\
			commands:
				- missing
				- find 
				- rotate
			argument: string representation of a json format
				- '{"arrays": [1,2,3....], "rotate": 2 -> (for rotate function)}'
			
			example: python cli.py -c rotate -a '{"arrays": [1,2,3,4], "rotate": 4}'
			'''
		)
	)

	parser.add_argument("-c", "--command", required=True, help="command to execute")
	parser.add_argument(
		"-a", "--argument", help="Accept json data as string(inclose in single quote)."
		)
	args = parser.parse_args()
	process_command(args)
	