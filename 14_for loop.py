# for loop in Python

name = "Anindya"
for i in name:
    print(i)

# nested for loop
colors = ['Blue', 'Red', 'Green']
for j in colors:
    print(j)
    for k in j:
        print(k)


# range() function

for k in range(5):  # will print from 0 -> 4
    print(k)

for i in range(5):   # now prints 1 to 5
    print(i+1)

for i in range(2, 9):      # will print from 2 to 8 (start, end)
    print(i)

for i in range(2, 9, 2):   # (start, end, step) -> (i=2; i<9; i+=2) of C/C++
    print(i)
