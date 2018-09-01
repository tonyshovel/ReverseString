#This file is written clearly and reverse a sentence by reverse.
#reversed_messages = "Can you reverse these messages ?"
def reverse_whole(messages):
	def reverse_sing(single_word):
		sing_w = list(single_word)
		sing_w.reverse()
		sing_w = ''.join(sing_w) 
		return sing_w 
	messages = messages.split(" ")
	for i in range(len(messages)):
		messages[i] = reverse_sing(messages[i])
	return (" ".join(messages)).lower()
#print(reverse_whole(reversed_messages))
#OUTPUT = nac ouy esrever eseht segassem ?
