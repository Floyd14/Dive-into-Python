#importing Sys
import sys
print(sys.version)      

def fib(n):
    '''
    Funzione che calcola la serie di Fibonacci'''
    print 'n =', n
    if n > 1:
        return n * fib(n - 1)
    else:
        print 'end of the line'
        return 1

# ES: LIST COMPREHENSION
# Definisco una funzione 
def buildConnectionString(params):
    """
    Build a connection string from a dictionary of parameters.
    Returns string.
    """
    return "\n".join(["%s = %s" % (k, v) for k, v in params.items()]) 
                #join() concatena le stringhe
                #params.items() return una LISTA di TOUPLES [(k1, v1), (k2, v2), ...]
                #[filtro]



#Controllo. Tutti i moduli hanno un attributo: __name__.module ecc
if __name__ == "__main__":   
    # Definisco un dictionary..
    myParams = {"server":"mpilgrim", \
                "database":"master", \
                "uid":"sa", \
                "pwd":"secret" \
                }

print buildConnectionString.__doc__ # Attributo __doc__    
print buildConnectionString(myParams)
print fib(5)




