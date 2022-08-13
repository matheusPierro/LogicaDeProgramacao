#Representa todo momento em que o algoritmo precisa interagir com o usuario
# Exibe "Meu primeiro programa"
print("Meu primeiro Programa")
# Exibe o número 12
print(12)

nome = "Edson"
idade = 48
peso = 85.64

# Forma 1
print("1. O meu nome é", nome, "tenho", idade, "anos e ", peso, "Quilos")

# Forma 2
print("2. O meu nome é {} tenho {} anos e {} Quilos".format(nome, idade, peso))
print("2. O meu nome é {0} tenho {1} anos e {2:.1f} Quilos".format(nome, idade, peso))
print("2. O meu nome é {n} tenho {i} anos e {p:.2f} Quilos".format(n=nome,i=idade,p=peso))

# Forma 3
print(f"3. O meu nome é {nome} tenho {idade} anos e {peso:.2f} Quilos")