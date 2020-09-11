file=open("prg14.txt","r")

emp_no=int(input("Enter Emp_no :"))
print("\n{:8} {:8} {:10} {:10} {:10} {:8} {:10}".format("Emp_no","Name","Dept_no","Basic","DA","HRA","Conveyance"))
for line in file:
	value=line.split()
	if(str(emp_no)==value[0]):
		for i in value:
			print(i.ljust(10),end="")
		print("\n")

file.seek(0)

dept_no=int(input("Enter Dept_no :"))
print("\n{:8} {:8} {:10} {:10} {:10} {:8} {:10}".format("Emp_no","Name","Dept_no","Basic","DA","HRA","Conveyance"))
for line in file:
	value=line.split()
	if(str(dept_no)==value[2]):
		for i in value:
			print(i.ljust(10),end="")
		print("\n")
