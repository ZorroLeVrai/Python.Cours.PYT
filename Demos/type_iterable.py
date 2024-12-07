class Counter:
    def __init__(self, start, end):
        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self): 
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num - 1
                       
if __name__ == '__main__' :
    a, b = 2, 5
    c1 = Counter(a, b)
    c2 = Counter(a, b)
    
    # Sans l'utilisation de iter()
    print("Print the range without iter()")
    
    for i in c1:
        print(i, end ="\n")
    
    print("\nPrint the range using iter()")
    
    # Avec utilisation de iter()
    obj = iter(c2)
    try:
        while True: # Print till error raised
            print (next(obj))
    except: 
        # Imprimer un message spécifique lors de l'exception StopIteration
        print ("\nFin de la boucle")
