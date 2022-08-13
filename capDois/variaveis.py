#Em python não declaramos as variáveis com um tipo. Sua tipagem é dinâmica, ou seja, no decorrer do programa ela pode assumir conteúdo de tipos diferentes.
nome = "Edson"      # Tipo Texto (string)
salario = 1234.56   # tipo real (float)
qtd_filhos = 2      # tipo inteiro (int)
opcao = 's'         # tipo caractere
maioridade = True   # tipo lógico

# Utilizando casting para modificar o tipo da variável
x = "55"            # x é do tipo string e vale '55'
x = float(x)        # x passou a ser float e vale 55.0
x = str(x)          # x voltou a ser string
x = int(x)          # x passou a ser int e vale 55

# UTILIZANDO VARIÁVEIS DIFERENTES E DESCOBRINDO OS TIPOS
nome = "Edson"      # Tipo Texto (string)
print(f"A variável nome = {nome} é do tipo {type(nome)}")
salario = 1234.56   # tipo real (float)
print(f"A variável salario = {salario} é do tipo {type(salario)}")
qtd_filhos = 2      # tipo inteiro (int)
print(f"A variável qtd_filhos = {qtd_filhos} é do tipo {type(qtd_filhos)}")
opcao = 's'         # tipo caractere
print(f"A variável opcao = {opcao} é do tipo {type(opcao)}")
maioridade = True   # tipo lógico
print(f"A variável maioridade = {maioridade} é do tipo {type(maioridade)}")

# UTILIZANDO A MESMA VARIÁVEL E DESCOBRINDO O SEU TIPO DEPOIS DE UM CASTING
x = "55"            # x é do tipo string e vale '55'
print(f"x = {x} e é do tipo {type(x)}")
x = int(x)          # x passou a ser int e vale 55
print(f"x = {x} e é do tipo {type(x)}")
x = str(x)          # x voltou a ser string
print(f"x = {x} e é do tipo {type(x)}")
x = float(x)        # x passou a ser float e vale 55.0
print(f"x = {x} e é do tipo {type(x)}")