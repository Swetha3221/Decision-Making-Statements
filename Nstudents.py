'''
'''

 There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
'''
'''
Ans:
# Input for seating capacities of the labs and number of students
x = int(input())  # Seating capacity of L1
y = int(input())  # Seating capacity of L2
z = int(input())  # Seating capacity of L3
n = int(input())  # Number of students


suitable_lab = None
max_usage = -1


if x >= n:
    usage = x - n
    if usage > max_usage:
        max_usage = usage
        suitable_lab = "L1"

if y >= n:
    usage = y - n
    if usage > max_usage:
        max_usage = usage
        suitable_lab = "L2"

if z >= n:
    usage = z - n
    if usage > max_usage:
        max_usage = usage
        suitable_lab = "L3"


print(suitable_lab)
'''
'''
