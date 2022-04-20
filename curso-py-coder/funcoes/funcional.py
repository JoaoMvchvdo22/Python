def soma(a, b):
    return a + b


somar = soma
print(somar(3, 4))


def operacao_binaria(fn, op1, op2):
    return fn(op1, op2)


resultado = operacao_binaria(soma, 13, 48)
print(resultado)
