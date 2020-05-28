
p=['a:A','b:B','c:C','d:D']
count=0
for x in p:
    count+=1
    print(count,end=")   ")
    #print(x)
    b=x.split(":")
    print('{0[0]:<5}{0[1]:<17}'.format(b))