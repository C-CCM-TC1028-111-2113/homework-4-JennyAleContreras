def main():
    height = int(input("Enter triangle height: "))
    #escribe tu código abajo de esta línea
    for i in range(1, height + 1):
        for j in range(height - i):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        print()
    pass

if __name__ == '__main__':
    main()
