# i want to find a word is a palimdrome or not
string = int(input("enter a word:"))
i = 1
sum = 0
while(i <= string):
    sum = sum + i
    i += 1
print("the sum is:", sum)
if string == string[::-1]:
    print("the word is palindrome")
else:
    print("the word is not palindrome")
while(i<=num):

    sum=sum+i

    i+=1
print("the sum is:",sum)
