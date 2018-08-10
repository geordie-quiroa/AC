from math import floor as f, log2 as log

possible_heap = [16,14,10,8,7,9,3,2,4,0]
#n = f(lg(len(possible_heap)))
#i = pow(2,n)-1
#i = pow(2,n)
#print("Total elementos %i" %len(possible_heap))
#print("utlimo nivel padre empezando desde 1 nivel %i"%n)
#print("Ultimo nodo a evaluar en arreglo antes de %i" %i)
#print("Ultimo nodo padre a evaluar en %i" %s)

is_heap=[1]

def controlador_de_verificacion(p_h):

    n=len(p_h)
    #print(n)
    i=0
    while i < (f(n/2)-1):
        if is_heap[0] == 0:
            break
            #exit()
        else:
            evaluar_nodo_padre(p_h, i)
        i+=1
    i=f(n/2)-1
    if (2*i)+1 == n-1 and is_heap[0] != 0:
        if p_h[i] >= p_h[(2*i)+1]:
            is_heap[0] = 1
    if (2 * i)== n - 2 and is_heap[0] != 0:
        if p_h[i] >= p_h[(2*i)+1]:
            is_heap[0]=1
        else:
            is_heap[0]=0
    if is_heap[0] == 1:
        print("El arreglo representa un heap.")
    else:
        print("El arreglo no representa un heap.")

def evaluar_nodo_padre(p_h, i):
    #print(i)
    if (p_h[i] >= p_h[(2*i)+1]): #and (p_h[i-1] >= p_h[f(i * 2)]):
        if (p_h[i] >= p_h[f(i * 2)+2]):
            pass
        else:
            is_heap[0]=0


controlador_de_verificacion(possible_heap)
#print(is_heap[0])

