user_name=input('\tBienvenido a la calculadora de IMC (Indice de Masa Corporal). \n\nPor favor ingresa tu nombre: ')
weight=int(input('¿Cuánto pesas?: '))
height= float(input('¿Cuánto  mides?: '))
wait_msg = 'Calculando... por favor espere'
print(wait_msg*2)
imc = round(weight/(height**2),2)
print(f"{user_name}:\n>Tu peso es: {weight}\n>Tu estatura es: {height}\n>Tu IMC es: {imc}")
if imc<18.5:
    print('Según tus resultados de IMC tu peso es bajo.')
elif (imc>=18.5) and (imc<25):
    print('Según tus resultados de IMC tu peso se considera normal.')
elif (imc>=25) and (imc<30):
    print('Según tus resultados de IMC tienes sobrepeso.')
elif imc>=30:
    print('Según tus resultados de IMC padeces de obesidad.')