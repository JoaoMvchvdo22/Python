trabalho_terca = True
trabalho_quinta = False

'''
- Os dois sendo verdadeiros = TV'50 + sorvete
- Só um sendo verdadeiro = TV'32 + sorvete
- Nenhum verdadeiro = Fica em casa
'''
tv_50 = trabalho_terca and trabalho_quinta
svt = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not svt

print('Tv50={}, Tv=32={}, Sorvete={}, Saudável={}'.format(
    tv_50, tv_32, svt, mais_saudavel))
