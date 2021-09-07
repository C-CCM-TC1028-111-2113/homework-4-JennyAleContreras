def Minimo(n):
    minimo = min(n)
    return minimo
    
def main():
    num = int(input("Escribe un numero : "))
    #escribe tu código abajo de esta línea
    for n in range(0, num):
        if (n*n)>num:
            print(n)
            print(Minimo(n))
    pass

if __name__ == '__main__':
    main()
