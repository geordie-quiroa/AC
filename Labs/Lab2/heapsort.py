output=open("heapsort.txt", "a")
from math import floor as f, log2 as log
website_page_rank = [3,39,61,91,57,22,75,89,9,90,63,78,28,73,20]
contador=[0]
contador_prog=[0]

def max_heapify(a,i):
    counter(1)
    program_counter(1)
    largest=0
    l=(i*2)+1
    r=(i*2)+2
    counter(1)
    if l<= (len(a)-1) and a[l] > a[i]:
        counter(1)
        largest=l
    else:
        counter(1)
        largest=i
    if r<= (len(a)-1) and a[r]> a[largest]:
        counter(1)
        largest = r
    if largest != i:
        counter(1)
        a[i]=a[largest]
        max_heapify(a, largest)
    #print(a, i)

def build_max_heap(a):
    counter(1)
    program_counter(1)
    a_length=len(a)
    i=f(a_length/2)
    for count in range (i, -1, -1):
        counter(1)
        max_heapify(a, count)
    output.write(str(a))
    #print(a)

def counter(a):
    contador[0]+=a

def program_counter(a):
    contador_prog[0] += a

build_max_heap(website_page_rank)

r="Total de iteraciones en lineas de codigo: %s"%contador + "\nTotal de valores en el arreglo: %i" %(len(website_page_rank))
s= "\nNxLog(N) = %f" %(len(website_page_rank)*log(len(website_page_rank)))
p="\nTotal de iteraciones del programa como tal: %s"%contador_prog
print(r,s, p)
output.write('\n'+ r + '\n'+ s + '\n'+ p )
