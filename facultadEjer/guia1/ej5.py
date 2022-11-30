
def filasI(n):
    for x in range(n):
        for j in range(n):
            print('*' , end=' ')
        print()

def filasP(n):
    for x in range(n):
        for j in range(x):
            print('*' , end=' ')
        print()



def __main__():
    num = int(input('ingresar numero'))
    filasI(num)
    filasP(num)




#programa main
if __name__ == "__main__":
    __main__()