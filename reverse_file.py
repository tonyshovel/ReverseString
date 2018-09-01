def reverse_string(messages):
	messages = list(messages)
	messages.reverse()
	messages = "".join(messages).split(" ")
	messages.reverse()
	return " ".join(messages)
def main():
	try:
		file_reverse = open("reverse_messages.txt","r")
	except:
		file_reverse = open("reverse_messages.txt","w+")
	finally:
		if file_reverse.mode == "r":
			 file_content = file_reverse.read()
			 file_content = reverse_string(file_content)
			 file_reverse.close()
			 file_reverse = open("reverse_messages.txt","w")
			 if len(file_content) == 0:
			 	no_content = "There was nothing in this file !"
			 	file_reverse.write(reverse_string(no_content).lower())
			 	file_reverse.close()
			 else:
			 	file_reverse.write(file_content.lower())
			 	file_reverse.close()
		if file_reverse.mode == "w+":
			not_exist = "This file was not exist !"
			file_reverse.write(reverse_string(not_exist).lower())
			file_reverse.close()
main()
