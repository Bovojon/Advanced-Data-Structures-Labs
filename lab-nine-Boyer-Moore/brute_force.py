import time

input_file = "Pbar_1.0_scaffolds.fa" # Input file for the text

with open(input_file, 'r') as text_file:
    text = text_file.read().replace('\n', '')

def find_first(pattern, text):
    length_text = len(text)
    length_pattern = len(pattern)

    for index_start in range(length_text):
        index_end = index_start + length_pattern

        if text[index_start:index_end] == pattern:
            return index_start

    return "The pattern is not present in the text"

def find_all(pattern, text):
    length_text = len(text)
    length_pattern = len(pattern)
    list_index = []

    for index_start in range(length_text):
        index_end = index_start + length_pattern

        if text[index_start:index_end] == pattern:
            list_index.append(index_start)

    if list_index:
        return list_index
    else:
        return "The pattern is not present in the text"

def test_funcs():
	print("Testing of the functions: ")

	result = find_first("TTTTT", text)
	print("Find_first for TTTTT returns: {}".format(result))

	result = find_all("TTTTT", text)
	print("Find_all for TTTTT returns: {}".format(result))

	result = find_first("ZZZZZ", text)
	print("Find_first for ZZZZZ returns: {}".format(result))

	result = find_all("ZZZZZ", text)
	print("Find_all for ZZZZZ returns: {}".format(result))

def timed_test():
	short_string = "TTTGGTCACC"
	long_string = "AAGAAACTTTATTGGAGGCGGTGTTGGGACTGGATGAACCATTTATCC"

	start_time = time.time()
	find_all(short_string, text)
	print("Time for find_all with a short pattern (10 characters): {} s.".format((time.time() - start_time)))

	start_time = time.time()
	find_all(long_string, text)
	print("Time for find_all with a long pattern (48 characters): {} s.".format((time.time() - start_time)))



#------------------------- Main Program --------------------------

prompt_loop = True

while prompt_loop:
	action = input("\n------------- Input ------------ \n1 to search for a pattern [first occurence] \n2 to search for a pattern [all occurences] \n3 to test the functions \n4 to run the timed test \n5 to quit: ")

	if action == "1":
		pattern = input("What pattern to search for: ")
		first_index = find_first(pattern, text)
		print("The first time the pattern occurs is at index {}.".format(first_index))
	elif action == "2":
		pattern = input("What pattern to search for: ")
		list_index = find_all(pattern, text)
		print("The indices at which the pattern occurs are {}.".format(list_index))
	elif action == "3":
		test_funcs()
	elif action == "4":
		timed_test()
	elif action == "5":
		prompt_loop = False
	else:
		print("Invalid Input")
