import sys
import string
arguments = list(sys.argv)

worklist = []
d = {}
max_length = 3

if len(arguments) ==2:
	max_length = 3
	filename = arguments[1]
else:
	max_length = int(arguments[1][2:])
	filename = arguments[2]


def read_in():
	grammar = []
	gram = 0
	count = 0
	start = ""
	for line in open(filename, "r"):
		grammar.append(line.split("\n"))
		#grammar[count].pop()

	for aline in grammar:
		input = aline[0].split(" ",2)
		d.setdefault(input[0], []).append(input[2])

	start = list(d)[0];
	worklist.append(start)

	return d

def the_process():
	while (len(worklist)>0):
		current_array = worklist.pop().split(' ')

		# if the length of the current array is too long (compare it to max_length)
		if(len(current_array) > max_length):
			continue

		leftmost_nonterminal_index = 0
		for string in current_array:
			if string in d:
					break
			else:
				leftmost_nonterminal_index +=1

		if leftmost_nonterminal_index >= len(current_array):
				print(current_array)
				continue

		leftmost_nonterminal = current_array[leftmost_nonterminal_index]

		for replacement in d[leftmost_nonterminal]:
			NT_copy = list(current_array)
			NT_index = leftmost_nonterminal_index

			NT_copy.pop(NT_index)
			
			count = 0
			for number in replacement.split(" "): 
				NT_copy.insert((NT_index + count), number)
				count += 1

			string = ""
			for thing in NT_copy:
				string += thing + " "
			string = string[:-1]
			worklist.append(string)

read = read_in()
the_process()