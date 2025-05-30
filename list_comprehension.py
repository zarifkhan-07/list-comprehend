l=[1,2,3,4,5]
print(l)
even=[x for x in l if x%2==0]
print("Even",even)
odd=[x for x in l if x%2!=0]
print("Odd",odd)