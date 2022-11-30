listaA= [1,5,2,4]
listaB = [5,8,4,2]

#slicing
listaA += listaB
listaA[::2] = listaA[:len(listaA)//2]
listaA[1::2]=listaB
print(listaA)