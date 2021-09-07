def main():
  #escribe tu código abajo de esta línea
  temp = 0
  num = 0
  promedio = 0.0
  while True:
      num=float(input())
      if(num > -1):
          promedio = promedio+num
          temp = temp+1
      else:
          print(promedio / (temp))
          break
if __name__ == '__main__':
    main()
