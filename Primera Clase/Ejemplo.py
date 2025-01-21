total_chocolates = 0

for dia in range(1, 8):
    chocolates = int(input("Ingrese la cantidad de chocolates producidos en el día {}: ".format(dia)))
    total_chocolates += chocolates

cajas = total_chocolates // 12
sobrantes = total_chocolates % 12

print("José necesita {} cajas y sobrarán {} chocolates.".format(cajas, sobrantes))