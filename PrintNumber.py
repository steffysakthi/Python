num = input("Enter your number: ")
print( "number"+" "+num)
for i in range (1 ,100):

    if i%2==0 :
         print(i)
name =input("enter urname: ")
size= len(name)
reverse=""
for char in name:
    reverse = char + reverse
print(reverse)
if name==reverse:
    print("palidrome")
else:
    print("not palidrome")
