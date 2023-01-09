file1=open("text.pl")
file=file1.readlines()
# print(file)


group=[]
for line in file:
    if line.rstrip().isnumeric():
        group.append(line.rstrip())
    