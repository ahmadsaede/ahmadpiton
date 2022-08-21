# zeros = [[0 for c in range(3)] for r in range(2)]
#
# for x in range(len(zeros)):
#     for y in range(3):
#         print(zeros[x][y],end='')
#     print()

# def divs(a):
#     n=a
#     for i+1 in range(a):
#         yield a//(n)
#         n = n-1

def divs(a):
    for i in range(a):
        if(a%(i+1)==0):
            yield i+1



ls = divs(15)
print(*ls)


file = open("C:\\Users\\p\\Desktop\\xtfile.txt",'r+') #this is adress dehi motlaq a
# file.close()
# print(file.read())
s = open("C:\\Users\\p\\Desktop\\testAhmad.txt",'a') #tavajoh faghat dar halate a ,file w age mojood nabashe misaze
matn = file.read();
s.write(matn)
print(file.read())
print(s);