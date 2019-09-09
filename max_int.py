#algorithm for max_int

max_int = 0

num_int = 0

while True:
    num_int = int(input("Input a number: "))

    if num_int>= max_int:
        max_int = num_int


    if num_int < 0:
        break


print("The maximum is", max_int)    # Do not change this line
