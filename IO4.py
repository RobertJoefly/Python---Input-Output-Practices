"""Write a code to get the input in the given format and print the output in the given format
Input Description:
First-line indicates two integers separated by space. Second-line indicates three integers separated by space.
Third-line indicates three integers separated by space
Output Description:
Print the input in the same format.
Sample Input :
2 5
2 5 6
2 4 5
Sample Output :
2 5
2 5 6
2 4 5"""

a,b = input().strip().split(' ')
c,d,e= input().strip().split(' ')
f,g,h = input().strip().split(' ')

print(a,b)
print(c,d,e)
print(f,g,h)