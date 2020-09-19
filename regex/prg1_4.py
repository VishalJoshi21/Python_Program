import re
prog = re.compile('www[.]\D+[.]\D{,3}')
str=input("Enter web domain: ")
result = prog.search(str)
if result:
	print(result.group())
else:
	print("NONE")
