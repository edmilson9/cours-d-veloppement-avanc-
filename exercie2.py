import random
def devine ():
    count = 0
    a = random.randint(1, 100)
    x = int(input("saisir un nombre entre 1 et 100"))
    while x != a:
        if count == 4:
            print ("Le nombre est entre" ,a-random.randint(10,19), "et ", a+random.randint(10,19))
        x = int(input("saisir le nombre"))
        count+=1
#devine()

p = []
with open ("Mots.txt") as m:
    for i in m :
        p.append(i)
print(p)

def sorte(l):
    print(l == sorted(l))
#sorte(p)

def find(word, l):
    for i in l:
        if word == i:
            print(l.index(i))
#find("UN\n", p)
#find("DEUX\n", p)

def dicho (l, word):
    for i in range(len(l)//2):
        if word == l[i]:
            print(i)
            break



dicho(p, "UN\n")