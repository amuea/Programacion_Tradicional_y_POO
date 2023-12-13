# Programación Tradicional

def ingresar_temperaturas(self):
    temperaturas = [dia]
    for dia in range(1, 25):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Entrada de datos
temperaturas_tradicional = ingresar_temperaturas(1, 25)

# Cálculo y salida
promedio_tradicional = calcular_promedio_semanal(temperaturas_tradicional)
print(f"El promedio semanal de temperatura es: {promedio_tradicional}")
