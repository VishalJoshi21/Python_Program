start=int(input("Enter start number :"));
end=int(input("Enter end number :"));

for i in range(start,end):
	flag=0;
	for j in range(2,start):
		if i%j==0:
			for k in range(2,j):
				if j%k==0:
					flag=flag+1;
	if flag==0:
		print(i," ",end=" ")
	