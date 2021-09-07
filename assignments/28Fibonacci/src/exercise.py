from math import sqrt

def fib(index):
    if index < 2:
        return index
    else:
        u = ((1+sqrt(5))/2)
        j = ((u**index-(1-u)**index)/sqrt(5))
        return round(j)

def main():
    #escribe tu código abajo de esta línea
    index=int(input("Enter the index: "))

    print(fib(index))

    pass

if __name__=='__main__':
    main()
