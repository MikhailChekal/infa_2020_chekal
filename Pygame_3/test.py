d = {}
name = input("type your name: ")
f = open("records.txt")
count = 25
d.update({name: count})
f.write(d)
