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

# def divs(a):
#     for i in range(a):
#         if(a%(i+1)==0):
#             yield i+1



# ls = divs(15)
# print(*ls)


# file = open("C:\\Users\\p\\Desktop\\xtfile.txt",'r+') #this is adress dehi motlaq a
# file.close()
# print(file.read())
# s = open("C:\\Users\\p\\Desktop\\testAhmad.txt",'a') #tavajoh faghat dar halate a ,file w age mojood nabashe misaze
# matn = file.read();
# s.write(matn)
# print(file.read())
# print(s);


# file = open("/Users/ahmad/Desktop/aa.txt","r+")
# with open("/Users/ahmad/Desktop/aa.txt","r+") as f : # baraye close kardane khod kare file
# print(file.read(5))
# print(file.read(5))az edame ghabli ta akhar error am nemide age az (5)az tedade baghi monde character ha bishtar bashe
# print(file.read(5))
# print(file.read(5))
# print(file.read(5))
# print(file.read(5))
# print(file.read(5))
# print(file.read(5))
# print(file.read(5))

# lines = []
# while True :
#    line = file.readline()
#    if not line : # or if line == ''
#     break
#    lines.append(line)

# lines.reverse()
# for line in lines :
#     print(line,end='')

# file.close() 


# f = open("ahmad.txt","w")
# print(f.tell())
# f.write("salam")
# print(f.tell())
# print(f.write("ali"))
# print(f.tell())

# f = open("ahmad.txt","a")
# print(f.tell())
# print(f.write("ali"))
# print(f.tell())

# f = open('reza.txt','a')
# print(f.tell())
# print(f.write('ahmad'))
# print(f.tell())
# f = open("ahmad.txt","r")
# print(f.tell())

# f = open("ahmad.txt", "r")
# print(type(f))#file object
# l, r = (int(x) for x in input().split())#in bahale
# f.seek(l)
# s = f.read(r - l + 1)
# print(s)
# ------------- age masalan 70 milyooon khat bashe data e ----------------
# def csv_reader(path):
#     file = open(path)
#     result = file.read().split("\n")
#     return result #---- khata hafeze mide 


def csv_reader(path):
    with open(path) as file:
        for row in file: # read nakarde k !!??? soal konam
            yield row # dooone doone mindazim biroon


for i in csv_reader("ahmad.txt"):
    print(i)