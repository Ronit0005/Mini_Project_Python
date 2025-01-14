import time 
print("""Hii welcome to K-Mean Algorithm
      I would help you to find the best cluster for your data""")
time.sleep(5)
print('Enter the data one by one which you want to cluster')
noOfData = int(input('Enter the number of data you want to cluster: '))
i=1
data=[]
grp1=[]
grp2=[]
while i<=noOfData:
    data.append(int(input('Enter the data: ')))
    i+=1
for i in range(noOfData):
    if i==0:
        leader1=data[i]
        grp1.append(leader1)
    elif i==1:
        leader2=data[i]
        grp2.append(leader2)
    else:
        sum=0
        for d in grp1:
            sum=sum+d
        leader1=sum/len(grp1)
        for h in grp2:
            sum=sum+h
        leader2=sum/len(grp2)
        if abs(data[i]-leader1)<abs(data[i]-leader2):
            grp1.append(data[i])
        else:
            grp2.append(data[i])
print(f'The cluster 1 is: {grp1}')
print(f'The cluster 2 is: {grp2}')