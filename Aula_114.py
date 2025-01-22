# Higher Order Functions 
# Funçoes de primeira classe

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'Bom dia', 'Anderson')
)

print(
    executa(saudacao, 'Boa Noite', 'Anderson Saldanha')
)