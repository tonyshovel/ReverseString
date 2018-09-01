def reverse_string(messages):
	messages = list(messages)
	messages.reverse()
	messages = "".join(messages).split(" ")
	messages.reverse()
	return " ".join(messages)
