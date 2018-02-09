a="hello.world@good,bye"
count=0
n=len(a)
for i in range(0,n):
	if(a[i]=='.' or a[i]==',' or a[i]=='@' or a[i]=='!'or a[i]=='$' or a[i]=='%' or a[i]=='&'):
		count=count+1
print(count)		
