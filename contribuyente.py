#Práctica A - Enunciado
nom=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
sueldo_mensual=float(input("Ingrese su sueldo mensual: "))
print(f"Hola, {nom}!")
año_nacimiento=2025-edad
print(f"Naciste en: {año_nacimiento}")
sueldo_anual=sueldo_mensual*12
print(f"Sueldo anual: {sueldo_anual}")
if sueldo_anual>10000000:
    print("Eres contribuyente.")
else:
    print("No eres contribuyente.")