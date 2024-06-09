from colorama import init, Fore
init(autoreset=True)

def menu ():
    menu = """
    Bem vindo ao BANCO CENTRAL!
    Operações disponíveis:
    1. Depósito
    2. Saque
    3. Extrato
    4. Sair do Banco
    Digite a operação desejada: """
    return input(menu)

def depositar_dinheiro(saldo, extrato, /):
    try:
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato +=Fore.GREEN +f"\nDepósito: + R${valor:.2f}"
            print(Fore.GREEN + "Depósito realizado com sucesso!")
        else:
            print(Fore.YELLOW + "Por favor, informe um valor válido")
        return saldo, extrato
    except ValueError:
        print(Fore.RED + "Por favor, digite um valor numérico!")
        
def sacar_dinheiro(limite_saque, saldo, numero_saques, extrato, /):
    print(Fore.BLUE + "*** Você possui um limite de 3 saques diários! ***")
    print(Fore.BLUE + "*** Você possui um limite 500 reais por saque! ***")
    valor = float(input("Digite o valor do saque: "))
    
    excedeu_limite = numero_saques == limite_saque
    excedeu_saldo = valor > saldo
    excedeu_delimitadores = valor < 0 or valor > 500
    
    if excedeu_limite:
        print(Fore.RED + "Você excedeu seu número de saques diários!")
    elif excedeu_saldo:
        print(Fore.RED + "Você não possui saldo suficiente!")
    elif excedeu_delimitadores:
        print(Fore.RED + "Digite um valor válido!")
    else:
        numero_saques += 1
        saldo -= valor
        extrato += Fore.RED + f"\nSaque: - R${valor:.2f}"
        print(f"numero atual de saque: {numero_saques}")
    return saldo, extrato, numero_saques
def main():
    LIMITE_SAQUE = 3
    saldo = 0
    extrato = ""
    numero_saques = 0
    while True:
        try:
            opcao = menu()
            if opcao == "1":
                saldo, extrato = depositar_dinheiro(saldo, extrato)
            elif opcao == "2":
                saldo, extrato, numero_saques = sacar_dinheiro(LIMITE_SAQUE, saldo, numero_saques, extrato)
            elif opcao == "3":
                print("x---------------Extrato---------------x")
                print(extrato)
                print((Fore.GREEN if saldo > 0 else Fore.RED) + f"Saldo atual: R${saldo}")
                print("x-------------------------------------x")
            elif opcao == "4":
                print(Fore.YELLOW + "Fechando sistema...")
                break
            else:
                print(Fore.YELLOW + "Opção inválida, tente novamente!")
        except ValueError:
            print(Fore.RED + "Por favor, digite um valor numérico!") 
    print(Fore.GREEN + "Sistema fechado com sucesso")
main()