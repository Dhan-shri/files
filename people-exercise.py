# my_file=open("people-exercise.txt")
# data=my_file.read()
# print(data)
# my_file.close()

# f=open("people-exercise.txt")
file = open("people-exercise.txt", "r")

line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()
print(line_count)
