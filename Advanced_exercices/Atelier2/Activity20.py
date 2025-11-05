adresses_ip = ["192.168.0.1", "10.0.0.1", "172.16.0.1", "200.100.50.1", "169.254.0.1"]

#Q1
print(f"La premiere adresse dans la liste est {adresses_ip[0]}")

#Q2
print(f"La derniere adresse dans la liste est {adresses_ip[-1]}")

#Q3
print(f"La troisieme adresse dans la liste est {adresses_ip[2]}")

#Q4
adresses_ip.append("172.31.0.1")

#Q5
adresses_ip.remove("200.100.50.1")

#Q6
print(f"Le nombre d'addresses restants dans la liste apres les modifications est {len(adresses_ip)}")

#Q7
if "192.168.0.1" in adresses_ip:
    print(f"\"192.168.0.1\" est dans la liste")
else:
    print(f"\"192.168.0.1\" n'est pas dans la liste")

#Q8
adresse = "10.0.0.1".split(".")
if int(adresse[0]) > 0 and int(adresse[0]) < 127:
    print(f"{".".join(adresse)} est de class A")
elif int(adresse[0]) >= 128 and int(adresse[0]) <= 192:
    print(f"{".".join(adresse)} est de class B")
    if int(adresse[0]) == 169 and int(adresse[2]) == 254:
        print(f"{".".join(adresse)} est une adresse de lien local (APIPA)")
elif int(adresse[0]) >= 192 and int(adresse[0]) <= 223:
    print(f"{".".join(adresse)} est de class C")

#Q9
adresses_ip.sort()
print(f"La list par ordre croissant: {adresses_ip}")

#Q10
count1 = 0
for i in adresses_ip:
    i = i.split(".")
    if int(i[0]) >= 192 and int(i[1]) <= 223:
        count1 += 1
if count1 == len(adresses_ip):
    print("Toutes les adresses IP de la liste appartiennent a la classe C")
else:
    print(f"Seulement {count1} adresses IP appartiennent a la classe C")

#Q11
count = 0
for i in adresses_ip:
    i = i.split(".")
    if not (int(i[0]) == 169 and int(i[1]) == 254):
        count += 1
print(f"Le nombre des adresses IP publiques dans la liste est {count}")



# Classe A : [1.0.0.0, 126.255.255.255] (publique)
# Classe B : [128.0.0.0, 191.255.255.255] (publique)
# Classe C : [192.0.0.0, 223.255.255.255] (publique)
# Adresse IP de lien local (APIPA) : [169.254.0.1, 169.254.255.254] (locale)
