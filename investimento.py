depo = 50
total = 0
for mes in range(1,6):
    total = total + depo
    print(f"Mês: {mes} saldo total: R${total}")
print(f"Ao final de {mes} meses, você terá R${total}")