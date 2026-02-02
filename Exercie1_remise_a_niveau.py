nom =input("Saisir votre nom : ")
print(nom)

def mult (n, p):
    for i in range(p):
        print(i ,"x" ,n, "=", i*n)
mult(10, 3)

def div (n):
    t = []
    for i in range (n):
        if i!=0 and n%i== 0:
            t.append(i)
    if len(t) > 1:
        return False
    else :
        return True
div(13)

def prime():
    p = []
    i = 2
    while len(p) < 100:
        if div(i):
            p.append(i)
        i += 1
    print(p)
prime()

def phare(m, n):
    tot = 2*(m*n) * 5 * 7
    print("Pour ", m, " marches de ", n, " centimètres il parcourt ", tot/100, "m par semaine")
phare(20, 10)

def valide():
    saisie = input("Saisir une chaine d'adn : ")
    for l in saisie:
        if l not in "atgc":
            print("x")
            return False
        
    print("V")
    return True
valide()
    
     