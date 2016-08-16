# 12156 STRHH - Half of the half


number = int(input("Enter the number of test cases: "))
line=[]                             # making a list to contains all the strings
for i in range(number):
    line.append(input("Enter the strings of 2*k length: "))

# print(line) # print the list

for stg in line:
    print(stg[0:int(len(stg)/2):2])        
