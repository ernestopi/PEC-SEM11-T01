def populacao(a, b):
    ano = 0
    while True:
        ano += 1
        a += a * 0.02
        b += b * 0.03
        if b > a:
            break
    return ano

def main():
    populacao_a = float(input())
    populacao_b = float(input())
    if populacao_a < populacao_b:
        populacao_a, populacao_b = populacao_b, populacao_a
    print(populacao(populacao_a, populacao_b))

if __name__ == '__main__':
    main()
