a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços? ',a.isspace())
print('É númerico? ',a.isnumeric())
print('É alfabético? ',a.isalpha())
print('É alfanúmerico? ',a.isalnum())
print('Só ta em maiúsculas? ',a.isupper())
print('Só ta em minúsculas? ',a.islower())
print('Está capitalizada?',a.istitle()) #capitalizada(nem maiusculas nem minusculas)
