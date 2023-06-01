s=input("user input")
str=s.split()
min=len(str[0])
# print(min)
for i in str:
    if len(i)<min:
        min=len(i)
        print(i)