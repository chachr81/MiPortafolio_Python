# Concatenar frases en una oración

palabra1 = 'Treinta'
palabra2 = 'Días'
palabra3 = 'de'
palabra4 = 'Python'
espacio = ' '
frase = print(palabra1 + espacio + palabra2 + espacio + palabra3 + espacio + palabra4)

palabra1 = 'Codificando'
palabra2 = 'para'
palabra3 = 'todos'
espacio = ' '
otrafrase = print(palabra1 + espacio + palabra2 + espacio + palabra3)

company = "Codificando para todos"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[3:22])
print('Codificando' in company)
print(company[0:11])
print(company.find('Codificando'))
print(company.replace('Codificando', 'Enseñando'))
print(company.replace('Enseñando', 'Codificando'))
print(company.split(', '))
print(company[0])
print(company[21])
print(company[10])
print(company.index('C'))
print(company.index('f'))
print(company.rfind('o'))
frase = 'You cannot end a sentence with because because because is a conjunction'
print(frase.index('because'))
print(frase.rfind('because'))
frase1 = "30DaysOfPython"
frase2 = "thirty_days_of_python"
print(frase1.isidentifier())
print(frase2.isidentifier())
librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
librerias_r = '#, '.join(librerias)
print(librerias_r)

