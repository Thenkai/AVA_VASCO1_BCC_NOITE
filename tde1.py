# Autores: Gabriel Antony; Jonas O. Assis; Patrick Froes

arquivo = open("tristreaza.txt", "r").readlines()
print("")

vezes = int(arquivo[0])

for i in range(vezes):
    operacao = str(arquivo[1 + (i * 3)]).replace("\n", "")
    set1 = set(arquivo[2 + (i * 3)].replace("\n", "").split(","))
    set2 = set(arquivo[3 + (i * 3)].replace("\n", "").split(","))

    if operacao == "U":
        uniao = set1 | set2
        print(f"União: conjunto 1 {set1} conjunto 2 {set2}. Resultado: {uniao}".replace("\'", ""))
    elif operacao == "I":
        inter = set1 & set2
        print(f"Interseção: conjunto 1 {set1} conjunto 2 {set2}. Resultado: {inter}".replace("\'", ""))
    elif operacao == "D":
        difer = set1 - set2
        print(f"Diferença: conjunto 1 {set1} conjunto 2 {set2}. Resultado: {difer}".replace("\'", ""))
    elif operacao == "C":
        cart = {(x, y) for x in set1 for y in set2}
        print(f"Produto Cartesiano: conjunto 1 {set1} conjunto 2 {set2}. Resultado: {cart}".replace("\'", ""))
    else:
        print("Operação inválida.")

print("")