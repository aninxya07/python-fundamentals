# do-while loop : A loop that executes at least once, no matter what the condition is

# do {
#     // code block to be executed
# } while (condition);

# there's no do while loop in Python like it is in C/C++ or Java
# But we can achieve the similar function by modifying the existing while loop

i=0
while True:
    print(i, end=" ")
    if(i==0):
        break

# so the first time the loop gets executed (classic do while loop behaviour)
# but after going through the condition it became false, and it exited (while part of do-while loop)


i=0
while True:
    print(i, end=" ")
    i+=1
    if(i%10 == 0):
        break
print("\n")


while True:
    num = int(input("Enter a positive number: "))
    print(num)
    if(num<=0):
        break