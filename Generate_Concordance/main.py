#!/bin/python3
import re
from collections import Counter

#
# Complete the 'generateAndPrintConcordance' function below.
#
# The function accepts STRING_ARRAY inputLines as parameter.
#

inputLines = ["This is a test.", "This is a random test for study.", "How many sentences are there in this input?",
			  "List the word counts and what sentences they are found in.", "Sort them in alphabetical order."]


# method to build the concordance data for printing
def build_concordance_data(word_list, sentence_list):
	# initialize the concordance
	temp_concordance = []

	# loop through each word in the list
	for item in word_list:

		# initialize our sentence number to 1 (the first sentence)
		sentence_number = 1

		# initialize a temp_list to hold sentence numbers in which each word appears
		temp_list = []

		# loop through each sentence in the sentence_list
		for sentence in sentence_list:


			# create a list of words in the sentence for iterating through each word
			sentence = list(re.sub(r'[^\w\s]', '', sentence).split())

			# iterate through each word and evaluate it against the item (word) from the word_list_sorted
			for word in sentence:
				if item == word.lower():

					# append the sentence number to the temp_list for each time the item (word) appears in this sentence
					temp_list.append(sentence_number)

			# increment the sentence_number before moving to the next sentence in the list
			sentence_number += 1

		# once through the list of sentences we append the item (word), the value of the item
		# the value of the item here is the number of times this word appeared in the input
		# also appending the temp list or server list for each time the word appeared in the sentence
		temp_concordance.append([item, word_list[item], temp_list])

	return temp_concordance


def generateAndPrintConcordance(inputLines):
	# Write your code here

	# parse the individual words from the input and store them in a list removing any punctuation
	word_list = []

	# loop through each sentence and add each word to th word_list
	for sentence in inputLines:
		temp_list = re.sub(r'[^\w\s]', '', sentence).split()
		for word in temp_list:
			word_list.append(word)

	# set all the words to lowercase (so capitalized words aren't sorted first when alphabetizing)
	# sort the words alphabetically
	# remove duplicate words from the list and make a unique list of words with count for number time appeared
	# create a dictionary from the list
	word_list_sorted = dict(Counter(sorted([word.lower() for word in word_list])))

	# call the build_concordance_data for printing
	concordance = build_concordance_data(word_list_sorted, inputLines)

	# loop through the concordance data to print it out
	for data in concordance:
		# assigning values in the data and converting int values to strings for printing out each line
		word = data[0]
		num_times_appeared = str(data[1])
		server_list = ','.join(str(num) for num in data[2])

		# print out each item in the data in the required format
		print(f'{word}: {{{num_times_appeared}:{server_list}}}')


if __name__ == '__main__':

	generateAndPrintConcordance(inputLines)
