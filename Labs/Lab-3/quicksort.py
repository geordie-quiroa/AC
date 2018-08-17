from math import floor as f
unsorted_array = [5,10,15,32,55,21,40,2,3,76,89,28,9,7]
n = len(unsorted_array)-1
def quicksort(A, p, r):
    i = p
    j = r
    q = f((A[i] + A[j])/2)
    #print(A[i], A[j], q)
    while i < j:
        while A[i] < q:
            i+=1

        while A[j] > q:
            j-=1

        if i <= j:
            x = A[j]
            #print(x)
            A[j] = A[i] #switch
            A[i] = x
            #print("A[i] & A[j]: ", A[i], A[j])
            #print(A)
            i+=1
            #print(i)
            j-=1
            #print(j)
    if p < j:
        A = quicksort(A, p, j)
    if r > i:
        A = quicksort(A, i, r)
    return A
    #print(A)

def print2console():
    print("Arreglo original: %a" %unsorted_array)
    print("Arreglo ordenado: %a" %quicksort(unsorted_array, 0, n))
#print(quicksort(unsorted_array, 0, n))

print2console()