def num_sorte(nasc):
    soma = 0
    while nasc > 0:
        soma += nasc % 10
        nasc = int(nasc / 10)
    return soma

def main():
    data = int(input())
    print(num_sorte(data))

if __name__ == '__main__':
    main()