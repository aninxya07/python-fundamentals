# Break and Continue statement in Python

# break : Sometimes during a particular iteration we want to exit completely from the loop
# break ex : up to i=9 done now break, but it was supposed to go till i=15

# continue : Sometimes during a particular iteration we want to skip the current iteration and continue the same process from the next iteration of the loop
# coninue ex : like i=1 done, now skip i=2 step and start for i=3

# break

for i in range(12):
    print(i, end=" ")
    if(i==10):
        break
print("\n")


# continue
for i in range(10):
    if(i==8):
        print("Skip sorry")
        continue
    print(i)


# another example
for i in range(10):
    if(i==8):   # it'll skip the iteration where i=8, means 5 x (8+1) = 5x9 = 45 will be skipped
        print("Skipping this iteration")
        continue
    print("5 x", i+1, "=", 5*(i+1))



