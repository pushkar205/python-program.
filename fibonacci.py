n=10
n1=0
n2=1
count=0
if n<=0:
	print("enter a positive number")
elif n==1:
	print("fibonacci sequence upto 10 terms",n,":")
	print(n1)
else:
	print("fibonacci sequence upto 10",n,":")
	while count < n:
		print(n1,end=',')
		nth = n1+n2

		n1 = n2
		n2 = nth
		count +=1
