#Faça um programa que leia um nome de usuário e a sua senha e 
#não aceite a senha igual ao nome do usuário, 
#mostrando uma mensagem de erro e voltando a pedir 
#as informações.

login = input('Login:')
senha = input('Senha:')

while login == senha:
    print('Sua senha deve ser diferente do login querida')
    senha = input('Senha:')

print('Cadastro aprovado')
 