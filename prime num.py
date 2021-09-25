num = int(input("enter a value:"))

for i in range(2,num):
    if num%2==0:
        print("not prime num.")
        break
else:
    print("it's prime num")