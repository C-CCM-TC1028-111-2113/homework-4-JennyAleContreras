def simbolos(i):
    if (i%2==0):
        return ("%")
    else:
        return ("#")

def main():
  #Write your code below this line
    num = int(input())
    for i in range(1, num+1):
        print(i,"-",simbolos(i))

    pass
if __name__ ==  "__main__":
    main()
