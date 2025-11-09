import argparse

# Crear una generador sintáctico de variables para la terminal 
parser = argparse.ArgumentParser(description= "Programa que devuelve el número de pares deseados")
parser.add_argument("n", type=int, help= "Numero de valores pares deseados")

# Traductor variable sintactica a python
args = parser.parse_args()

# Ajustar código original
num = 0
for i in range(args.n):
  num += 2
  print(num)

