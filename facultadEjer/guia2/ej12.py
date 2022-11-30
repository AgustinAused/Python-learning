

def crear():
    lisSoc=[]
    lisVis=[]

    numSocio=int(input("Ingrese el número de socio"))
    while numSocio!=0:
        while (numSocio<10000 or numSocio>99999) and numSocio!=0:
            numSocio=int(input("Ingrese el número de socio válido"))
        pos=buscar(lisSoc,numSocio)
        if pos!=-1:
            lisVis[pos] += 1 
        else:
            lisSoc.append(numSocio)
        
        numSocio=int(input("Ingrese el número de socio"))
    return lisSoc, lisVis

def buscar(lisSoc,numSocio):
    if len(lisSoc==0):
        return -1
    else:
        for x in range(len(lisSoc)):
            if lisSoc[x]==numSocio:
                return x 
            else:
                return -1

def imprimirListas(lisSoc, lisVis):
    for x in range(len(lisSoc)):
        print(lisSoc[x], lisVis[x])

def eliminar(lisSoc,lisVist):
    nSoc= int(input('ingresar número de socio '))
    while(nSoc <10000 or nSoc>99999):
        nSoc = int(input('ingresar número de socio (ingresar número de 5 digitos)'))
    pos = buscar(lisSoc,nSoc)
    if (pos != -1):
        lisSoc.pop(pos)
        lisVist.pop(pos)
    return lisSoc,lisVist

def main():
    lisSocios,lisVisitas=crear()
    imprimirListas(lisSocios,lisVisitas)
    lisSocios,lisVisitas=eliminar(lisSocios,lisVisitas)
    imprimirListas(lisSocios,lisVisitas)

main()