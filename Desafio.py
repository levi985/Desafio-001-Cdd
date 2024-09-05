h1 = int(input("Digite a primeira hora:"))
m1 = int(input("Digite o primeiro minuto: "))
h2 = int(input("Digite a segunda hora:"))
m2 = int(input("Digite o segundo minuto: "))
if h1 > 12:
    h1 = h1-12
if h2 > 12:
    h2 = h2-12
if m1 > 60:
    m1 = m1-60
if m2 > 60 :
    m2 -= 60
sh = (h1 + h2)
sm = (m1 + m2)
if sm >= 60:
    sm -= 60
    sh += 1
if sm >12:
    sm -=12
print(f" {sh} : {sm}")
