import time

# Input file for the text
# input_file = "Pbar_1.0_scaffolds.fa"
input_file = "sequence-1.dat"

with open(input_file, 'r') as text_file:
    text = text_file.read().replace('\n', '')

def find_first(pattern, text):

    stringT_len = len(text)
    pattern_len = len(pattern)

    if pattern_len == 0:
        return "Empty string is at index 0"
    else:
        index_dict = {}
        for a in range(pattern_len):
            index_dict[pattern[a]] = a
        a = pattern_len-1

        i = pattern_len-1
        while i < stringT_len:
            if text[i] == pattern[a]:
                if a==0:
                    return i
                else:
                    i -= 1
                    a -= 1
            else:
                j = index_dict.get(text[i], -1)
                i += pattern_len - min(a, j+1)
                a = pattern_len - 1

        return "[Substring not found]"


def find_all(pattern, text):

    stringT_len = len(text)
    pattern_len = len(pattern)
    list_of_indices = []

    if pattern_len == 0:
        print("Empty string is at index 0")
    else:
        index_dict = {}
        for a in range(pattern_len):
            index_dict[pattern[a]] = a
        a = pattern_len-1

        i = pattern_len-1
        while i < stringT_len:
            if text[i] == pattern[a]:
                if a==0:
                    list_of_indices.append(i)

                    j = index_dict.get(text[i], -1)
                    x = min(a, j+1)
                    i += pattern_len - x
                    a = pattern_len - 1

                else:
                    i -= 1
                    a -= 1
            else:
                j = index_dict.get(text[i], -1)
                x = min(a, j+1)
                i += pattern_len - x
                a = pattern_len - 1
        if(len(list_of_indices)==0):
            return "[Substring not found]"
        else:
            return list_of_indices

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

    # find_first(str(sys.argv[1]), str(sys.argv[2]))
    # find_all(str(sys.argv[1]), str(sys.argv[2]))
