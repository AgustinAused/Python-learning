def ingresar():
    num1 = int(input('ingresar numero 1: '))
    num2 = int(input('ingresar numero 2: '))
    return num1,num2
def devolver(tupla):
    print(f'{tupla[0]}{tupla[1]}')

def main():
    nums = ingresar()
    devolver(nums)


#main program 
if __name__ == "__main__":
    main()