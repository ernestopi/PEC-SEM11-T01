def corrida(tartaruga):
    lebre = 0
    minutos = 0
    while True:
        minutos += 1
        tartaruga += 1
        lebre += 10
        if lebre > tartaruga:
            break
    return minutos
def main():
    tartaruga = int(input().strip())
    print(corrida(tartaruga))

if __name__ == '__main__':
    main()
