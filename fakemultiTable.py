import random
def multipier(itake):
    for i in range(1,11):
        multi = itake*i
        table.append(multi)
    
    # Generating false value
    falti=random.randint(table[0],table[9])
    
    # Adding false value at a nth position which was renerated randomly
    table.insert(n,falti)
    # removing the previous correct value 
    table.remove(table[n+1])
    return table

def solver():
    for i in range(1,11):
        solmulti = itake*i
        Ntable.append(solmulti)
    return Ntable

if __name__=='__main__':
    itake = int(input("Enter your number to get it's multiple table: "))
    table=[]
    Ntable =[]
    n=random.randint(1,8)
    print(multipier(itake))
    solver()
    # checking at which postion the table is wrong
    for j in range(10):
        if table[j] != Ntable[j]:
            print(f" Wrong multiplier at {j+1} its {table[j]}.\n correct result will be {Ntable[j]}.")
