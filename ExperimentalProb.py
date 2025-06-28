import random
fict = {}
for i in range(1_00_000):
    generater = random.randint(0,1)
    fict[generater]=fict.get(generater,0) +1
print("Probability of 0",float(fict[0]/1_00_000))
print("Probability of 1",float(fict[1]/1_00_000))