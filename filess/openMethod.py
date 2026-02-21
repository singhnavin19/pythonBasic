f=open("navin.txt")
# print(f.read())
f.seek(0)
# for line in f:
#     print(line)
f.seek(0)
for line in f.readlines():
    print(line.strip())
# f.seek(0)
# for line in f.readlines():
#     print(line)





