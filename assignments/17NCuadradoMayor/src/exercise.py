def main():
    num = int(input("Escribe un numero : "))
    #escribe tu código abajo de esta línea
    for N in range(num):
        if N*N>30:
            N=min(N)
            print(N)
    pass

if __name__ == '__main__':
    main()
