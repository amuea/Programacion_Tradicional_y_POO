# Programación Orientada a Objetos (POO)

class ClimaSemana:
    def __init__(self):
        self.temperaturas = [dia]

    def ingresar_temperaturas(self):
        for dia in range(1, 25):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.temperaturas.append(temp)

    def calcular_promedio_semanal(self):
        promedio = sum(self.temperaturas) / len(self.temperaturas)
        return promedio

# Creación de objeto
clima_poo = ClimaSemana(lluvia, sol)

# Entrada de datos
clima_poo.ingresar_temperaturas(1, 25)

# Cálculo y salida
promedio_poo = clima_poo.calcular_promedio_semanal(sum(self.temperaturas)) / (len(self.temperaturas))
print(f"El promedio semanal de temperatura es: {promedio_poo}")
