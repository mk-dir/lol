x=int(input("Enter Number:"))
# print(x)
divisors=[]

for each in range(x+1):
    if each>0 and x%each==0:
        divisors.append(each)


if len(divisors)>2:
    print(divisors)

else: print("Prime Number")

# Umecatch? :| :D