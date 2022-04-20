import keyword


def soma(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total


def resultado_final(**kwargs):
    status = 'Aprovado'
    if kwargs['nota'] >= 7:
        print(status)
    else:
        print('Reprovado')
    return f'{kwargs["nome"]} foi {status}'


print(resultado_final)
