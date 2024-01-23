##Case para Engenharia de Software Jr
#Kauane Mendes dos Santos


# Criação das funções operacao_e_resultado e processa_operacao
def operacao_e_resultado(operacao, valorA, valorB, resultado):
    return f'{valorA} {operacao} {valorB} = {resultado}'

def processa_operacao(operacao, valorA, valorB):
    resultado = eval (f'{valorA} {operacao} {valorB}')
    return resultado, operacao_e_resultado(operacao, valorA, valorB, resultado)

#Impressão de lista de operaçõoes a ser processada após cada calculo realizado
operacoes_realizadas = []

#Criação de uma pilha (Stack) para guardar o resultado de cada calculo efetuado a ser impresso no final
pilha_resultados = []

# Execução das operações
resultado_soma, operacao_soma = processa_operacao('+', 2, 3)
operacoes_realizadas.append(operacao_soma)
pilha_resultados.append(resultado_soma)

resultado_subtracao, operacao_subtracao = processa_operacao('-', 14, 8)
operacoes_realizadas.append(operacao_subtracao)
pilha_resultados.append(resultado_subtracao)

resultado_multiplicacao, operacao_multiplicacao = processa_operacao('*', 5, 6)
operacoes_realizadas.append(operacao_multiplicacao)
pilha_resultados.append(resultado_multiplicacao)

resultado_soma1, operacao_soma1 = processa_operacao('+', 2147483647, 2)
operacoes_realizadas.append(operacao_soma1)
pilha_resultados.append(resultado_soma1)

# Implementação da funcionalidade de divisão
resultado_divisao, operacao_divisao = processa_operacao('/', 18, 3)
operacoes_realizadas.append(operacao_divisao)
pilha_resultados.append(resultado_divisao)

# Exibição dos resultados
print('\nResultados:')
print(f'Resultado Soma: {resultado_soma}')
print(f'Resultado Subtração: {resultado_subtracao}')
print(f'Resultado Multiplicação: {resultado_multiplicacao}')
print(f'Resultado Soma1: {resultado_soma1}')
print(f'Resultado Divisão: {resultado_divisao}')

# Exibição das operações realizadas *em forma de lista
print('\nOperações realizadas:')
for operacao_realizada in operacoes_realizadas:
    print(operacao_realizada)

# Exibição pilha (stack) de resultados - lista Python
print('\nPilha de Resultados:')
for resultado in pilha_resultados:
    print(resultado)
