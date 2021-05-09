"""Write a code to get the input in the given format and print the output in the given format.
Input Description:
A single line contains a string.
Output Description:
Print the characters in a string separated by comma.
Sample Input :
guvi
Sample Output :
g,u,v,i"""

user = input()
for i in user[:len(user)-1]:
    print(i, end=',')
print(user[len(user)-1])