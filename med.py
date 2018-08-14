def median(l,k):
	l.sort()
	if(k%2==0):
			return l[k/2]
	else:
			return(l[k/2-1]+l[k/2])/2
k=int(raw_input())
l=[int(y) for y in raw_input().split()]
print(median(l,k-1))

			
