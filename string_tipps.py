
# Expression of string
# a string should be written between single quote or double quotes
course = "machine learning"

# using tripple quotes for multi-line strings
message = """
I am learning
maching learning
"""
print(course)
print(message)


# useful function and string index
# len(): get the length of a string
print(len(course))

# get the first letter of a string
print(course[0])

# get the last letter of a string
print(course[-1])

# get from the 1st letter to last letter of a string, but not including the last
print(course[0:-1])
print(course[:-1])

# get the 1st to 4th letter, but not including 4th
print(course[0:4])
print(course[:4])

# get the 2nd to 4th letter, but not including 4th
print(course[1:4])

# duplicate a string
print(course[0:])
print(course[:])


# useful string methods
course = " machiNe leaRning "

# convert all letters in a string to uppercase
print(course.upper())

# convert all letters in a string to lowercase
print(course.lower())

# convert the first letter of the word in a string to uppercase
print(course.title())

# remove the white space at the beginning and end of a string
print(course.strip())

# remove the white space only at the end of a string
print(course.rstrip())

# remove the white space only at the beginning of a string
print(course.lstrip())

# return the index of a character in a string
print(course.find("a"))

# return the index of a sequence in a string
print(course.find("lea"))

# replace character a in a string with b
print(course.replace("a", "b"))

# return if "mac" is in the string course
print("mac" in course)

# return if "mac" is not in the string course
print("mac" not in course)


# escape sequences in Python
escape_sequence = "machine \" learning"  # to escape " in a string
escape_sequence = "machine \' learning"  # to escape ' in a string
escape_sequence = "machine \\ learning"  # to escape \ in a string
escape_sequence = "machine \n learning"  # start a new line after \n


# formatted string
# using f”{} {} {} …” to concatenate strings between {}
last_name = "World"
first_name = "Hello"

full_name = f"{first_name}{'_'}{last_name}"
print(full_name)