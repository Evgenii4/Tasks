money = int(input("Ввести сумму вклада:"))

per_cent = {'ЕКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
for key in per_cent:
    per_cent[key] *= (money / 100)
max_cent = max(per_cent.values())

print(per_cent)
print("Максимальная сумма, которую вы можете заработать -", max_cent)

