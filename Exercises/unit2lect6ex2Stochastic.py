#Stochastic
import random
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print(mylist)
print('----------')
import random

# Code Sample A is deterministic
mylist = []
# when seed in inside the loop, everytime it generate the same number
# and since it's in the list, then add nothing
for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
		# different is here, compared to the first one
        if number not in mylist:
            mylist.append(number)
print(mylist)
print('----------')
    
    
# Code Sample B
mylist = []
# when seeed is outside the loop, everytime the loop is the same
# different is here, compared to the first one
random.seed(0)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
    print(mylist)