preço = float(input("Digite o preço do produto: ")) #casting
quantidade = int(input("Digite a quantidade comprada: "))

total= preço * quantidade

print(f"Valor total: R${total: 2f}")