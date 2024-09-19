'''
'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1
'''
'''
Ans:

a = int(input())  # Seating capacity of L1
b = int(input())  # Seating capacity of L2
c = int(input())  # Seating capacity of L3
allocated_lab = input().strip()  # Lab allocated for ACE training


if allocated_lab == "L1":
    min_capacity_lab = "L2" if b < c else "L3"
elif allocated_lab == "L2":
    min_capacity_lab = "L1" if a < c else "L3"
else:  # allocated_lab == "L3"
    min_capacity_lab = "L1" if a < b else "L2"


print(min_capacity_lab)
'''
'''
