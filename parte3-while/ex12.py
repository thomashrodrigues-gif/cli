

soma = 0
número = float(input("Digite o número (0 para sair)"))
               
while numero != 0:
    soma = soma + numero
    numero = float(input("Digite um numero (0 para sair): "))

print(f"A soma total é: {soma}")
