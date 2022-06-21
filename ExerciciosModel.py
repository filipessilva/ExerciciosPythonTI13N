
def exercicio01():
    A = 10
    B = 20
    msg = "Antes da Troca: A = {}, B = {}".format(A,B)
    aux = A
    A = B
    B = aux

    msg = msg + "\nDepois da Troca: A= {}, B = {}".format(A,B)
    return msg

def exercicio02():
    print ('Insira um numero para ver seu antecessor: ')
    num = int(input())
    return 'O antecessor é {}'.format(num-1)

def exercicio03():
    print ('Calcular Base * Altura')


    print ('Informe a base:')
    base = float(input())
    if base <= 0:
            return 'Digite um numero valido'

    print ('Informe a altura:')
    altura = float(input())
    if altura <= 0:
        return 'Digite um numero valido'

    return 'A area do retangulo é: {}'.format(base * altura)

def exercicio04():

    print('Conversor de idade em dias')
    print('Informe quanto anos você tem:')
    anos = int(input())
    if anos < 0:
        return 'Digite um numero valido'
    print ('Informe quantos meses você tem:')
    meses = int(input())
    if meses < 0:
        return 'Digite um numero valido'
    print('Informe quantos dias você tem:')
    dias = int(input())
    if dias < 0 :
        return 'Digite um numero valido'

    return 'O total de idade em dias: {}.'.format(anos*365 + meses * 30 + dias)

def exercicio05():

    print('Calculadora Eleitoral')
    print('Insira o numero total de eleitores:')
    eleitores = int(input())
    if eleitores < 0 :
        return 'Digite um numero valido'

    print ('Insira o numero de votos em  branco:')
    vbrancos = int(input())
    if vbrancos < 0 :
        return 'Digite um numero valido'
    msg = 'Porcentagem de votos em branco: {}'.format(vbrancos / eleitores * 100)

    print('Insira o numero de votos nulos:')
    vnulos = int(input())
    if vnulos < 0 :
        return 'Digite um numero valido'
    msg = msg + '\nPorcentagem de votos em nulo: {}'.format(vnulos/eleitores * 100)

    print('Insira o numero de votos validos:')
    vvalidos = int(input())
    if vvalidos < 0 :
        return 'Digite um numero valido'
    msg = msg + '\nPorcentagem de votos validos: {}'.format(vvalidos/eleitores * 100)

    if vbrancos + vnulos + vvalidos != eleitores:
        return 'O numero total de votos é diferente do total de eleitores!'

    return msg

def exercicio06():
    print('Calculadora de Reajuste Salarial')
    print('Escreva seu salario:')

    salario = float(input())
    if salario< 0 :
        return 'Digite um numero valido'

    print('Insira a porcentagem do reajuste salarial:')
    reajuste = float(input())
    if reajuste < 0 :
        return 'Digite um numero valido'

    return 'O valor do salario atualizado será: {}'.format(salario+(salario*reajuste)/100)

def exercicio07():
    print ('Custo Final do Carro ao Consumidor')
    print('Insira o valor de fabrica de um veiculo:')
    valor = float(input())
    if valor < 0 :
        return 'Digite um numero valido'
    return 'O valor final do veiculo será: {}'.format(valor + (valor*28)/100 + (valor*45)/100)

def exercicio08():

    print('Media Final')
    print('Insira a primeira nota:')
    A = float(input())
    if A < 0 :
        return 'Digite um numero valido'
    print('Insira a segunda nota:')
    B = float(input())
    if B < 0 :
        return 'Digite um numero valido'
    print('Insira a terceira nota:')
    C = float(input())
    if C < 0 :
        return 'Digite um numero valido'

    return 'A media final é {}'.format((A+B+C)/3)

def exercicio09():
    print ('Venda de Maçã')
    print('Insira o numero de maçãs desejadas:')
    maça = int(input())
    if maça < 0 :
        return 'Digite um numero valido'
    if maça < 12:
        return 'O valor da venda é {}'.format(maça * 1.30)

    return 'O valor da venda é {}'.format(maça * 1)

def exercicio10():