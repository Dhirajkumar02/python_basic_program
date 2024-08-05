x = "mom"
s = x.upper()
temp = ""
for i in s:
    temp = temp+i
if(s==temp):
    print("Palindrome")
else:
    print("Not Palindrome")