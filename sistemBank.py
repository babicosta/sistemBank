
#Depósito
#Deve ser possível depositar valores positivos para a minha conta.
#Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.


#Saque
#Deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque.
#Se não tiver saldo deve exibir mensagem informando que não tem saldo.
#Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

#Extrato
#Deve listar todos os dépositos e saques realizados.
#Deve exibir saldo atual da conta.
#Os valores devem ser exibidos utilizando o formato R$xxx.xx


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[x] Exit

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Valor do déposito:"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else: 
            print("ERRO! O valor informado é inválido.")
        
    elif opcao == "s":
        valor = float(input("Valor do saque:"))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("ERRO! Você não tem saldo suficiente!")
        
        elif excedeu_limite:
            print("ERRO! O valor do saque excede o limite.")
            
        elif excedeu_saque:
            print("ERRO! Número de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("ERRO! O valor informado é inválido.")
            
    elif opcao == "e":
        print("\n**************** EXTRATO ***************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("******************************************")
        
    elif opcao == "x":
        break
    
    else:
        print("ERRO! Por favor, selecione novamente a operação desejada.")