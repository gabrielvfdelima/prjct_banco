"""3 operações: Depósito, saque e extrato

Todos depósitos precisam ser armazenados em uma váriavel e impressos no extrato

Sistema permitirá apenas 3 saques diários, com o limite de 500 reais por saque
caso o usuário não tenha saldo em conta, o sistema deverá exibir uma mensagem 
informando que não foi possível realizar o saque por saldo insuficiente.

Todos os saques deverão ser armazenados em uma váriavel e exibidos na operação
extrato.

A operação extrato deve listar todos os depósitos e saques realizados na conta
e exibir o saldo atual da conta. Os valores devem ser exibidos usando o formato:
R$ xxx,xx
"""
from colorama import init, Fore
init()

#Menu do banco
menu = """
Bem vindo ao BANCO CENTRAL!
Operações disponíveis:
1. Depósito
2. Saque
3. Extrato
4. Sair do Banco
Digite a operação desejada: """

#Declaração e inicialização de variaveis
numero_saques = 0
saldo_em_conta = 0
dinheiro_depositado = []
dinheiro_sacado = []
LIMITE_SAQUE = 3

#Método para fazer o depósito do dinheiro
def depositar_dinheiro():
    #Acessando variaveis globais
    global saldo_em_conta, dinheiro_depositado
    
    #Declarando e inicializando variável para guardar valor de depósito
    deposito = 0
    
    #Bloco try para verificar se o usuário digitou um tipo de dado válido
    try:
        #Input na variável depósito
        deposito = float(input("Digite quanto dinheiro você quer depositar:"))
        
        #Verifica se o valor do depósito é maior que zero
        if deposito > 0:
            
            #Armazena o depósito na lista de depósitos
            dinheiro_depositado.append(deposito)
            
            #Incrementa o depósito no saldo em conta
            saldo_em_conta += deposito
            
            return Fore.GREEN + "Depósito realizado com sucesso!" + Fore.RESET
        else:
            return Fore.RED + "Digite um valor válido!" + Fore.RESET
    except ValueError:
        return Fore.RED + "Por favor, insira apenas valores numéricos!" + Fore.RESET

#Método para sacar o dinheiro
def sacar_dinheiro():
    #Acessando as variaveis globais
    global LIMITE_SAQUE, saldo_em_conta, dinheiro_sacado, numero_saques
    
    #Bloco try para verificar se o usuário digitou um tipo de dado válido
    try:
        #Verifica se atingiu o número de saques diários
        excedeu_limite = numero_saques == LIMITE_SAQUE
        #Verifica se o valor do saque é menor que o saldo em conta
        sem_saldo_suficiente = saque < saldo_em_conta
        #Verifica a delimitação dos valor para o saque
        fora_da_delimitacao = saque > 0 and saque < 500
        
        if excedeu_limite:
            #Avisos para o usuário
            print(Fore.RED + "Você pode sacar no máximo 500 reais por saque!")
            print(f"Você só tem 3 saques diários! Quantia de saques atual: {numero_saques}" + Fore.RESET)
            
            #Input na variável saque
            saque = float(input("Digite quanto dinheiro você quer sacar: ")) 
            
            if sem_saldo_suficiente:
                
                if fora_da_delimitacao:
                    dinheiro_sacado.append(saque)
                    saldo_em_conta -= saque
                    numero_saques+=1
                    
                    return Fore.GREEN + "Saque realizado com sucesso!" + Fore.RESET
                else: 
                    return Fore.RED + "Digite um valor válido" + Fore.RESET
            else:
                return Fore.RED + "Saldo insuficiente!" + Fore.RESET
        else:
            return Fore.YELLOW + "Você atingiu o limite de saques diários!" + Fore.RESET
    except ValueError:
        return Fore.YELLOW + "Por favor, insira apenas valores numéricos!" + Fore.RESET

def extrato():
    global dinheiro_depositado, dinheiro_sacado, saldo_em_conta
    
    #Exibindo todos os depósitos
    print(Fore.GREEN + "\nDepósitos:")
    for deposito in dinheiro_depositado:
        print(f"   + R$ {deposito:.2f}")
    
    #Exibindo todos os saques
    print(Fore.RED +"\nSaques:")
    for saque in dinheiro_sacado:
        print(f"   - R$ {saque:.2f}")
    
    #Verifica se o saldo é positivo ou negativo
    if saldo_em_conta > 0:
        #Exibindo saldo
        print(Fore.GREEN + f"\nSaldo Atual: R$ {saldo_em_conta:.2f}\n" + Fore.RESET)
    else:
        #Exibindo saldo
        print(Fore.RED + f"\nSaldo Atual: R$ {saldo_em_conta:.2f}\n" + Fore.RESET)

while True:
    operação = input(menu)
    if operação == "1":
            print(depositar_dinheiro())
    elif operação == "2":
            print(sacar_dinheiro())
    elif operação == "3":
            print("\nExtrato da Conta:")
            extrato()
    elif operação == "4":
            print("Fechando sistema...")
            break
    else:
            print("Operação inválida, tente novamente")
print("Sistema fechado")