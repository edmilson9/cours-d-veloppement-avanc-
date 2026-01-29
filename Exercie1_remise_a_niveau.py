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
        print(" Diviseurs propres : ", t)
    else :
        return print(n, "est premier")
div(13)

def phare(m, n):
    tot = 2*(m*n) * 5 * 7
    print("Pour ", m, " marches de ", n, " centimètres il parcourt ", tot, " par semaine")
phare(20, 10)