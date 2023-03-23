#ques-1
# The provided code stub reads two integers from STDIN,a and b. Add code to print three lines where:
#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.

a=int(input())
b=int(input())

print(a+b)
print(a-b)
print(a*b)

#ques-2
#The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,
# a//bin . The second line should contain the result of float division, a/b.
# No rounding or formatting is necessary.

a=int(input())
b=int(input())

print(a//b)
print(a/b)

# The included code stub will read an integer,n, from STDIN.
# Without using any string methods, try to print the following:
# 123...n
# Note that "..." represents the consecutive values in between.

n=int(input())

for i in range(1,n+1): 
    print(i,end="")

