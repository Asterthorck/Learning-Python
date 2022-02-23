x = input('Type 1 to convert from C to F or type 2 to convert from F to C: ')
y = int(x)

if y == 1 :
    c = input('Enter C: ')
    celcius = int(c)
    celciusresult = (celcius * (9/5)) + 32
    print(celciusresult,'F')

if y == 2 :
    f = input('Enter F: ')
    fahrenheit = int(f)
    fahrenheitresult = (fahrenheit - 32 ) * (5/9)
    print(fahrenheitresult,'C')

if y != 1 and y != 2 :
    print('Error!, please type 1 to convert from C to F or type 2 to convert from F to C')
#I intend to loop back at the begginin to give the user the option to try to intup again in case of placing a value different than 1 or 2
