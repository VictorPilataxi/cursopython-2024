
# Estructuras de Control - Reto Principiantes

menu = """
       ************************************************
       *          MENÚ DE LA APLICACIÓN               *
       ************************************************
       
       Elija el ejercicio del reto que desea ejecutar:
       1000: Hola Mundo!
       1001: Extremadamente básico
       1002: Área del Círculo
       1003: Suma Simple
       1004: Producto Simple
       1005: Promedio 1
       1006: Promedio 2
       1007: Diferencia
       1008: Salario
       1009: Salario con bonus
       1010: Cálculo Simple
       1011: Esfera		
       1012: Área
       1013: El Mayor
       1014: Consumo
       1015: Distancia Entre dos Puntos
       1016: Distancia
       1017: Combustible Gastado
       1018: Billetes
       1019: Conversión de Tiempo
       1020: Edad en Días
       1021: Billetes y Monedas
       1035: Prueba de Selección 1
       1036: Fórmula de Bhaskara
       1037: Intervalo
       
       0: Salir del Programa
"""

bandera = True

while bandera:
   print(menu)
   opcion = int(input("Elija una opción del menu: \n"))
   if opcion == 0:
      print("Hasta pronto!!")
      break
  
   elif opcion == 1000:
      #Ejercicio 1000
      print("Hello World!") 
  
   elif opcion == 1001:
      # Ejercicio 1001
      A = int(input("Ingrese #1 de la suma : \n"))
      B = int(input("Ingrese #2 de la suma : \n"))
      X = A + B
      print(f"X = {X}")
   
   elif opcion == 1002:
      # Ejercicio 1002
      pi = 3.14159
      radio = float(input("Ingrese el radio de la circunferencia: \n"))
      area = pi * radio**2
      print(f"A={area:.4f}")
   
   elif opcion == 1003:
      # Ejercicio 1003
      A = int(input("Ingrese el valor A: \n"))
      B = int(input("Ingrese el valor B: \n"))
      SOMA = A + B
      print(f"SOMA = {SOMA}")
   
   elif opcion == 1004:
      # Ejercicio 1004
      a = int(input("Ingrese el valor A: \n"))
      b = int(input("Ingrese el valor B: \n"))
      PROD = a * b
      print(f"PROD = {PROD}")
      
   elif opcion == 1005:
      # Ejercicio 1005
      A = float(input("Ingrese el valor A: \n"))
      B = float(input("Ingrese el valor B: \n"))
      MEDIA = (A*3.5/11) + (B*7.5/11)
      print(f"MEDIA = {MEDIA:.5f}")

   elif opcion == 1006:
      # Ejercicio 1006
      A = float(input("Ingrese el valor A: \n"))
      B = float(input("Ingrese el valor B: \n"))
      C = float(input("Ingrese el valor C: \n"))
      MEDIA = (A*0.2) + (B*0.3) + (C*0.5)
      print(f"MEDIA = {MEDIA:.1f}")

   elif opcion == 1007:
      # Ejercicio 1007
      A = int(input("Ingrese el valor A: \n"))
      B = int(input("Ingrese el valor B: \n"))
      C = int(input("Ingrese el valor C: \n"))
      D = int(input("Ingrese el valor D: \n"))
      DIFERENCIA = (A*B) - (C*D))
      print(f"DIFERENCIA = {DIFERENCIA}")

   elif opcion == 1008:
      # Ejercicio 1008
      num_empl = int(input("Ingrese el Còdio del Empleado: \n"))
      num_horas = int(input("Ingrese el Número de Horas laboradas: \n"))
      monto_hora = float(input("Ingrese el monto de cada hora çlaborada: \n"))
      SALARY = num_horas * monto_hora
      print(f"NUMBER = {num_empl}")
      print(f"SALARY = U$ {SALARY:.2f}")

   elif opcion == 1009:
      # Ejercicio 1009
      nombre = str(input("Ingrese el nombre del vendedor: \n"))
      salario = float(input("Ingrese el valor del salario: \n"))
      ventas = float(input("Ingrese el valor de las ventas realizadas: \n"))
      TOTAL = salario + (ventas*0.15)
      print(f"TOTAL = R$ {TOTAL:.2F}")

   elif opcion == 1010:
      # Ejercicio 1010
      producto_1 = input("Ingrese el Código, Número de Unidades y el Precio del Producto 1: \n")
      producto_2 = input("Ingrese el Código, Número de Unidades y el Precio del Producto 2: \n")
      valor_1 = producto_1.split(" ")
      valor_2 = producto_2.split(" ")       
      s_t_p1 = float(valor_1[1]) * float(valor_1[2])
      s_t_p2 = float(valor_2[1]) * float(valor_2[2])
      suma_final = s_t_p1 + s_t_p2          
      print(f"VALOR A PAGAR: R$ {suma_final:.2f}")
         
   elif opcion == 1011
      # Ejercicio 1011      
      R = int(input("Ingrese el valor del radio: \n"))
      pi = 3.14159
      c = 4/3
      v = c*pi*R**3
      print(f"VOLUME = {v:.3f}")

   elif opcion == 1012:
      # Ejercicio 1012
      A, B, C = map(float, input().split())
      pi = 3.14159
      print(f"TRIANGULO: {A*C/2:.3f}")
      print(f"CIRCULO: {pi*C**2:.3f}")
      print(f"TRAPEZIO: {(A+B)*C/2:.3f}")
      print(f"QUADRADO: {B*B:.3f}")
      print(f"RETANGULO: {A*B:.3f}")

   elif opcion == 1013:
      # Ejercicio 1013
      valores = input("Ingrese 3 valores para determinar el mayor: \n").split()
      a, b, c = map(int, valores)
      MayorAB = (a + b + abs(a - b)) // 2
      mayor = (MayorAB + c + abs(MayorAB - c)) // 2
      print(f"{mayor} eh o maior")

   elif opcion == 1014:
      # Ejercicio 1014
      X = int(input("Ingrese la distancia recorrida: \n"))
      Y = float(input("Ingrese el valor de combustible consumido: \n"))
      C = X/Y
      print(f"{C:.3f} km/l")

   elif opcion == 1015:
      # Ejercicio 1015
      x1, y1 = map(float, input("Ingrese las coordenadas del Punto 1: \n").split())
      x2, y2 = map(float, input("Ingrese las coordenadas del Punto 2: \n").split())
      distancia = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
      print(f"{distancia:.4f}")

   elif opcion == 1016:
      # Ejercicio 1016
      distancia = int(input("Ingrese la distancia recorrida, en Km: \n"))
      tiempo = distancia * 2
      print(f"{tiempo} minutos")
      
   elif opcion == 1017:
      # Ejercicio 1017
      h = int(input("Ingrese la cantidad de horas: \n"))
      v = int(input("Ingrese la velocidad media: \n"))
      l = h * v / 12
      print(f"{l:.3f}")
   
   elif opcion == 1018:
      # Ejercicio 1018
      valor = int(input("Ingrese el valor: \n"))
      billetes = [100, 50, 20, 10, 5, 2, 1]
      lista_billetes = {}
      for billete in billetes:
         lista_billetes[billete], valor = divmod(valor, billete)
      print(f"{sum(lista_billetes[b] * b for b in billetes)}")
      for billete, cantidad in lista_billetes.items():
         print(f"{cantidad} nota(s) de R$ {billete},00")

   elif opcion == 1019:
      # Ejercicio 1019
      t = int(input("Ingresa la duración del evento: \n"))
      horas = t // 3600
      minutos = (t % 3600) // 60
      segundos = (t % 3600) % 60
      print(f"{horas}:{minutos}:{segundos}")
      
   elif opcion == 1020:
      # Ejercicio 1020
      edad_dias = int(input("Ingrese la edad expresada en días: \n"))
      año = edad_dias // 365
      mes = (edad_dias % 365) // 30
      dias = (edad_dias % 365) % 30
      print(f"{año} ano(s)")
      print(f"{mes} mes(es)")
      print(f"{dias} dia(s)")
      
   elif opcion == 1021:
      # Ejercicio 1021
      valor = float(input("Ingrese el valor monetario: \n"))
      valores = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
      centavos = round(valor * 100)
      desglose = {}
      for valor in valores:
         valor_centavos = round(valor * 100)
         desglose[valor], centavos = divmod(centavos, valor_centavos)
      print("NOTAS:")
      for valor in valores[:6]:  
         print(f"{int(desglose[valor])} nota(s) de R$ {valor:.2f}")
      print("MOEDAS:")
      for valor in valores[6:]:  
         print(f"{int(desglose[valor])} moeda(s) de R$ {valor:.2f}")

   elif opcion == 1035:
      # Ejercicio 1035
      A, B, C, D = map(int, input("Ingrese los valores a comparar: \n").split())
      if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
         print("Valores aceitos")
      else:
         print("Valores nao aceitos")
      
   elif opcion == 1036:
      # Ejercicio 1036
      A, B, C = map(float, input("Ingrese los 3 valores: \n").split())
      discriminante = B**2 - 4*A*C
      if discriminante < 0 or A == 0:
         print("Impossivel calcular")
      else:
         R1 = (-B + discriminante**0.5) / (2*A)
         R2 = (-B - discriminante**0.5) / (2*A)
         print(f"R1 = {R1:.5f}")
         print(f"R2 = {R2:.5f}")

   elif opcion == 1036:
      # Ejercicio 1036
      n = float(input())
      if 0 <= n <= 25:
         intervalo = "Intervalo [0,25]"
      elif 25 < n <= 50:
         intervalo = "Intervalo (25,50]"
      elif 50 < n <= 75:
         intervalo = "Intervalo (50,75]"
      elif 75 < n <= 100:
         intervalo = "Intervalo (75,100]"
      else:
         intervalo = "Fora de intervalo"
      print(intervalo)

   else:
      print("La opcion seleccionada no existe!!!")
