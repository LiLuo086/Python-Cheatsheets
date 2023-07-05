# input() function can receive input from terminal
# usage: input(prompt): prompt is a string, representing the message before the input

x = input("please give x a value: ")
print(f"The value of x is {x}")

# The prompt of input() function is not necessary
# y = input()
# print(y)


# Python built-in type functions
print(int(x)+2)  # convert x to integer
print(float(x)+3.4)  # convert x to float
print(bool(x))  # convert x to boolean
print(str(x))  # convert x to string
print(type(x))  # return the type of x
