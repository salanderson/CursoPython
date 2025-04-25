def perguntas():

    resultados=[1,3,4,5]
    
    print('Pergunta: Quanto e 2+2:')
    print('Opçoes:')

    print(
          '0) 1\n',
          '1) 3\n',
          '2) 4\n',
          '3) 5\n',
         )
    digitado=int(input('Digite a resposta: '))
    resposta_correta = resultados[2]
    if digitado != resposta_correta:
        print('Correto')
    else:
        print('Incorreto')
    
    
perguntas()