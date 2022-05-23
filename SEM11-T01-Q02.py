def compra_carro(valor_carro):
    poupanca = 10000
    mes = 0
    while True:
        mes += 1
        valor_carro += valor_carro * 0.004
        poupanca += poupanca * 0.007
        if poupanca > valor_carro:
            break
    return mes

def main():
    carro = float(input())
    print(compra_carro(carro))

if __name__ == '__main__':
    main()