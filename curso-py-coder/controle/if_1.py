from traceback import print_tb


nota = float(input('Informe a nota do aluno: '))

if nota >= 9:
    print('Tenho duas palavras pra voce: Para béns :p')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5.5:
    print('Recuperação')
else:
    print('Reprovado')
print(nota)
