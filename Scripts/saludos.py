import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-saludo","--s", default = "", type = str)

args = parser.parse_args()

texto = args.s
texto = texto.upper()
value = random.random()
if texto == "HOLA":
    if value <= 0.5:
        print ("Hola, ¿cómo estas?")
    elif value <= 0.75:
        print("Mucho gusto, me llamo Computina")
    else:
        print("Disculpa pero no quiero hablar contigo")
else:
    print("Parece que tus padres no te enseñaron a saludar...")