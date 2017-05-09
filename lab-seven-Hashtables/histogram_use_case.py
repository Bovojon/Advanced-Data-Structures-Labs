'''
Jon
Use Case for a hash table
histogram_use_case.py

'''

# Open file to read words from
words = []
with open('critique-of-reason.txt','r') as f:
    for line in f:
        for word in line.split():
            words.append(word.lower())
histogram = {}

# Add each word and it's frequency into a dict
for word in words:
    histogram[word] = histogram.get(word, 0) + 1
first_10_list = []
for word, count in histogram.items():
    first_10_list.append([count, word])

# Get the 10 most frequent words
first_10_list.sort()
first_10_list.reverse()
first_10_list = first_10_list[:11]

# Normalize the data
max_int_len = len(str(first_10_list[0][0]))
max_count = first_10_list[0][0]
max_string = 0                              # Find longest string
for item in first_10_list:
    if len(item[1]) > max_string:
        max_string = len(item[1])
longest_star = 80 - 6 - 6 - max_string - max_int_len
ratio_top = longest_star/max_count
ratio_array = []
for i in first_10_list:
    ratio = i[0] * ratio_top
    ratio_array.append(int(ratio))
list_of_stars = []
for r in ratio_array:
    stars = '*'*r
    list_of_stars.append(stars)
# Draw the histogram
i = 0
for pair in first_10_list:
    print("%-6s %6d %s" % (pair[1], pair[0], list_of_stars[i]))
    i += 1
