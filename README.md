# Banco Central

Este é um sistema simples de banco em Python que permite aos usuários realizar três operações principais: depósito, saque e exibição de extrato. O sistema é projetado para gerenciar um saldo de conta e registrar todas as transações realizadas.

## Funcionalidades

- **Depósito**: Permite ao usuário depositar dinheiro na conta. Todos os depósitos são armazenados e exibidos no extrato.
- **Saque**: Permite ao usuário sacar dinheiro da conta, com um limite de três saques diários e um máximo de R$ 500 por saque. Se o saldo for insuficiente, o sistema notifica o usuário.
- **Extrato**: Exibe todos os depósitos e saques realizados, bem como o saldo atual da conta.

## Requisitos

- Python 3.x
- Biblioteca `colorama` para colorir as mensagens no terminal

## Instalação

1. Clone este repositório para a sua máquina local:
    ```bash
    git clone https://github.com/gabrielvfdelima/prjct_banco.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd banco-central
    ```
3. Instale a biblioteca `colorama`:
    ```bash
    pip install colorama
    ```

## Uso

Para iniciar o sistema bancário, execute o script `prjct_banco.py`:
#### Você verá o menu principal com as seguintes opções:
```bash
Bem vindo ao BANCO CENTRAL!
Operações disponíveis:
1. Depósito
2. Saque
3. Extrato
4. Sair do Banco
Digite a operação desejada:
```
#### Depósito
Selecione a opção 1 e insira o valor a ser depositado. O sistema confirmará se o depósito foi realizado com sucesso.

#### Saque
Selecione a opção 2 e insira o valor a ser sacado. O sistema verificará:

- Se o número de saques diários não foi excedido.
- Se o valor do saque é menor ou igual a R$ 500.
- Se há saldo suficiente na conta.

#### Extrato
Selecione a opção 3 para ver o extrato da conta, que mostrará todos os depósitos e saques, além do saldo atual.

#### Sair
Selecione a opção 4 para sair do sistema.

#### Exemplo de Execução

```
Bem vindo ao BANCO CENTRAL!
Operações disponíveis:
1. Depósito
2. Saque
3. Extrato
4. Sair do Banco
Digite a operação desejada: 1
Digite quanto dinheiro você quer depositar: 1000
Depósito realizado com sucesso!

Bem vindo ao BANCO CENTRAL!
Operações disponíveis:
1. Depósito
2. Saque
3. Extrato
4. Sair do Banco
Digite a operação desejada: 2
Você pode sacar no máximo 500 reais por saque!
Você só tem 3 saques diários! Quantia de saques atual: 0
Digite quanto dinheiro você quer sacar: 200
Saque realizado com sucesso!

Bem vindo ao BANCO CENTRAL!
Operações disponíveis:
1. Depósito
2. Saque
3. Extrato
4. Sair do Banco
Digite a operação desejada: 3

Extrato da Conta:
Depósitos:
   + R$ 1000.00

Saques:
   - R$ 200.00

Saldo Atual: R$ 800.00
```
## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

- Faça um fork do projeto
- Crie uma branch para sua feature (git checkout -b feature/nova-feature)
- Commit suas alterações (git commit -m 'Adiciona nova feature')
- Faça um push para a branch (git push origin feature/nova-feature)
- Abra um Pull Request