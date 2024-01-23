##Case para Engenharia de Software Jr
#Kauane Mendes dos Santos


# Criação das funções operacao_e_resultado e processa_operacao
def operacao_e_resultado(operacao, valorA, valorB, resultado):
    return f'{valorA} {operacao} {valorB} = {resultado}'

def processa_operacao(operacao, valorA, valorB):
    resultado = int (eval(f'{valorA} {operacao} {valorB}'))
    return resultado, operacao_e_resultado(operacao, valorA, valorB, resultado)

#Impressão de lista de operaçõoes a ser processada após cada calculo realizado
operacoes_realizadas = []

#Criação de uma pilha (Stack) para guardar o resultado de cada calculo efetuado a ser impresso no final
pilha_resultados = []

# Execução das operações
resultado, operacao = processa_operacao('+', 2, 3)
operacoes_realizadas.append(operacao)
pilha_resultados.append(resultado)

resultado, operacao = processa_operacao('-', 14, 8)
operacoes_realizadas.append(operacao)
pilha_resultados.append(resultado)

resultado, operacao = processa_operacao('*', 5, 6)
operacoes_realizadas.append(operacao)
pilha_resultados.append(resultado)

resultado, operacao = processa_operacao('+', 2147483647, 2)
operacoes_realizadas.append(operacao)
pilha_resultados.append(resultado)

# Implementação da funcionalidade de divisão
resultado, operacao = processa_operacao('/', 18, 3)
operacoes_realizadas.append(operacao)
pilha_resultados.append(resultado)

# Exibição das operações realizadas *lista Python
print('\nOperações realizadas:')
for operacao_realizada in operacoes_realizadas:
    print(operacao_realizada)

# Exibição pilha (stack) de resultados 
print('\nPilha de Resultados:')
for resultado in pilha_resultados:
    print(resultado)

