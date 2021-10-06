egyik = int(input('Adjon meg egy számot')) 
másik = int(input('Adjon meg egy számot'))
jel = input('Addjon megy egy műveleti jelet')
print('A művelet eredménye:' , end =" ")
if jel == '+':
    print(egyik+másik)
elif jel == '-':
    print(egyik-másik)
elif jel == '%':
    print(egyik%másik)
elif jel == '/':
    print(egyik/másik)
elif jel == ">>":
    print(egyik>>másik)
