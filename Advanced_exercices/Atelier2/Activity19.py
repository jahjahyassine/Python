def f1(n):
    for i in range(n):
        print("Bonjour")
bjr = int(input("Combien de « bonjour » veux-tu ? "))
f1(bjr)


def f2(n):
    if n % 10 == 0:
        print(f"{n} est pas divisible par 10")
    else:
        print(f"{n} n'est pas divisible par 10")
div10 = int(input("Entrez le nombre: "))
f2(div10)


def f3(n):
    factorielle = 1
    for i in range(1, n + 1):
        factorielle *= i        
    return factorielle
factorielle = int(input("Entrez le nombre: "))
print(f"Le factorielle de {factorielle} est {f3(factorielle)}")


def f4(word):
    count = 0
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    for i in word:
        if i in voyelles:
            count += 1
    return count
word = input("Entrez le mot: ")
print(f"Le nombre de voyelles dans {word} est {f4(word)}")


def f5(n):
    for i in range(11):
        print(f"{n} * {i} = {n * i}")
num = int(input("Entrez le nombre: "))
f5(num)


def f6(word):
    return len(word)
word2 = input("Entrez le mot: ")
print(f"Le nombre de caracteres de {word2} est {f6(word2)}")


def f7(n):
    if n == 0 or n == 1:
        return n
    else:
        return f7(n - 1) + f7(n - 2)
fibonacci = int(input("Entrez le nombre: "))
print(f7(fibonacci))
