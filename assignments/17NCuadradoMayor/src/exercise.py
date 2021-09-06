def main():
    num = int(input("Escribe un numero : ",'1'))
    #escribe tu código abajo de esta línea
    for N in range(num):
        if N*N>30:
            print(min(N))
    pass

if __name__ == '__main__':
    main()
