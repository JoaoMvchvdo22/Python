True or False
7 != 3 and 2 > 3

# Tabela verdade do AND

# True
True and True
# False
True and False
# False
False and True
# False
False and False


# Tabela verdade do OR

# True
True or True
# True
True or False
# True
False or True
# False
False or False

# Tabela verdade do XOR (or exclusivo)

# False
True != True
# True
True != False
# True
False != True
# False
False != False

# Operador de Negação (unário)

# False
not True
# True
not False

# Exercício na prática
saldo = 1000
salario = 4000
despesa = 2967

meta = saldo > 0 and salario - despesa >= 0.2 * salario
print(meta)
