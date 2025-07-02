while(1):
    num = int(input())

    if num%2==0:
        if num%8==0:
            print("O número é par, mas é múltiplo de 8. Informe um número par não múltiplo de 8.")
        else:
            break
    else:
        print("O número não é par. Informe um número par não múltiplo de 8.")
            
print(f"O número fornecido foi {num} e ele é par e não múltiplo de 8.")