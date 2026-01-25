uptoTable=int(input("please enter upto table no"))

table=2
while(table<=uptoTable) :
    for no in range(1,11):
        print(table*no,end="\t")
    table=table+1