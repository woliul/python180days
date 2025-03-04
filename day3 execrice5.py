#Execrise 5
#Prevent Data Modification
from operator import index

country=("Bangladesh","China","England")
#Convert tuple to list
b=list(country)
#Adding Country into tuple
b.append("Spain")
#Repalcing Country into tuple
b[1]="Srilanka"
#Convert list to tuple
country=tuple(b)

print(country)