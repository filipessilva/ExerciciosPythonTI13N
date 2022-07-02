
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
    list = []
    for i in range(1, 11):
        valor = float(input('Digite um número: '))
        list.append(valor)
    return sorted(list)

def exercicio11():
    salario = float(input('Digite seu salário fixo em R$:'))
    vendas = float(input('Digite o total das suas vendas em R$: '))
    if vendas >= 1500.0:
            c5 = (5*(vendas-1500))/100
            c3 = (3*vendas)/100
            total = salario+c3+c5

            return 'Você atingiu sua meta ! Seu salário total será de R${}'.format(total)
    else:
            c3 = (3/vendas)*100
            total = salario + c3

            return 'Seu salário total será de R${}'.format(total)

def exercicio12():
    conta = int(input('Digite o número da sua conta:'))
    saldo = float(input('Digite seu saldo em R$:'))
    debito = float(input('Digite o débito que você possui em R$:'))
    credito = float(input('Digite seu crédito em R$:'))

    saldoatualizado = saldo - debito + credito
    if saldoatualizado >= 0:
        return 'Saldo Positivo, seu saldo é de R${}'.format(saldoatualizado)
    else:
        return 'Saldo Negativo, seu saldo é de -R${}' .format(saldoatualizado)

def exercicio13():
    n = int(input('Digite um valor entre 1 e 10: '))
    if n > 10:
        return 'Opção inválida, digite um valor entre 1 e 10'
    elif n<0:
        return 'Opção inválida, digite um valor entre 1 e 10'
    else:
        for i in range(1, 11):
            result = n*i
            print('{} * {} = {}'.format(n, i, result))

def exercicio14():
    n = int(input('Digite um número: '))
    for i in range(1, n+1):
        print(i)

def exercicio15():
    list = 0
    for i in range(1,11):
        n = int(input('Digite um número: '))
        if n<0:
            list += +1

    return '\nSua lista possui {} números negativos' .format(list)

def exercicio16():
    list = 0
    for i in range(1, 11):
        n = float(input('Digite um número: '))
        if n<40:
            list += n

    return '\nO resultado da sua soma é {}' .format(list)

def exercicio17():
    aux = 0
    quant = 0
    for i in range(1, 101):

        aux += i
        quant += +1
        result = aux/quantidade

    return '\n{} / {} = {}' .format(aux, quant, result)

def exercicio18():
   n = int(input('Quantos números deseja digitar? '))
   if n<=0:
       print('Obrigado!')
   else:
    aux3 = 0
    quant = 1

    maior = float(input('Digite um número: '))
    for i in range(2, n + 1):
        num = float(input('Digite um número: '))

        aux2 = maior
        aux3 += num
        quant += +1
        med = (aux2+aux3)/quant

        if num>maior:
            maior = num

    print ('O maior número foi {}, e a media dos numeros {}').format(maior,med)

def exercicio19():
    total = 0
    maior = 0
    list = []
    for i in range(20):
        nota = float(input('Informe a {}ª nota:'.format(i+1)))
        list.append(nota)
        if nota>10:
            print('Digite uma nota válida')
        elif nota<0:
            print('Digite uma nota válida')
        else:
            total += nota
            medg = total / 20

    for i in range(20):
       if list[i] > medg:
          maior += 1

    print('A média da turma foi {} e {} aluno(s) tiveram nota maior que a média.'.format(medg,maior))

def exercicio20():
    med = 0
    medf = 0
    meds = 0
    abaixo = 0

    habitantes = int(input('Digite a quantidade de habitantes: '))
    for i in range(1, habitantes+1):
        salario = float(input('Digite seu salário em R$: '))
        if salario<=150.0:
            abaixo = +1
        if meds<salario:
            meds = salario
        if salario<0:
            print('Salário inválido')
        filhos = int(input('Digite a quantidade de filhos que você possui: '))
        if filhos<0:
            print('Quantidade inválida')

        med += salario
        medf += filhos
    results = med/habitantes
    resultf = medf/habitantes
    resultm = (abaixo/habitantes)*100

    print('Média do salário da população: R${}'.format(results))
    print('Media de numero de filhos por habitante: {}'.format(resultf))
    print('Maior salario entre os habitantes: R$ {}'.format(meds))
    print('A porcentagem de pessoas com salario abaixo de R$150.0 é de: {}%'.format(resultm))
