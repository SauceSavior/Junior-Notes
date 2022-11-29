file1=open("studentDatabase.txt","r")
file=file1.readlines()

for line in file:
    front(line.rstrip())