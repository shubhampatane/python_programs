#This programes requires names.csv file
#Guess the bolllywood movie name, You have got 6 chances
def display(movie,found,error):
    l = []
    d = []
    dis = ""
    l.append("  ")
    for i in movie:
        if i in found:
            l.append(i)
            l.append("  ")
        elif not i.isalpha():
            l.append(i)
            l.append("  ")
        elif i==" ":
            l.append("     ")
        else: 
            l.append(" __ ")
    dis = dis.join(l)
    for i in dis:
        d.append(i)
    if "_" in d:
        print(dis)
    else:
        print("\n")
        print(dis)
        print("\n")
        print("#"*20)
        print("YOU WON")
        print("#"*20)
        print("\n")
        menu()
def display_msg(found,error):
    f = ""
    e = ""
    fo = []
    er = []
    for i in found:
        fo.append(i)
        fo.append(" ")
    for i in error:
        er.append(i)
        er.append(" ")
    f = f.join(fo)
    e  = e.join(er)
        
    print("Alphabets found are ",f)
    print("Alphabets guessed wrong are ",e)
        
    
    
def play():
    import random
    movie = []
    lt = []
    l = []
    from csv import DictReader
    with open("names.csv") as f:
        a1 = [row["title"] for row in DictReader(f)]
    #print(len(a1))
    for i in a1:
        g = []
        jt = []
        jt.append(i)
        if ":" in i:
            g = i.split(":")
            jt[0] = g[0]
        l.append(jt[0])
    #print(len(l))       
    r = random.randint(0,len(l)-1)
    found = set()
    error = set()
    li = l[r]
    li = li.upper()
    for i in li:
       movie.append(i)
    display(movie,found,error)
    
    while (len(error)<=5):
        print("\n")
        print("Guess an alphabet")
        display_msg(found,error)
        a = input()
        if a.isalpha():
            a = a.upper()
        if a in found:
            print("Charachter already used - It was correct")
        elif a in error:
            print("Charachter already used -It was an error")
            display(movie,found,error)
        elif a.isalpha() and len(a)==1:
            if a in movie:
                print("Aplhabet In Movie Name !!!!!!")
                found.add(a)
                display(movie,found,error)
            else:
                print("Aplhabet NOT in Movie Name")
                error.add(a)
                display(movie,found,error)
        else:
            print("Invalid Charachter")
            display(movie,found,error)
            
    print("\n")
    print("#"*20)
    print("YOU LOST")
    print("#"*20)
    print("\n")
    print("Movie Name is ")
    print("\n")
    dis = ""
    lt.append("  ")
    for i in movie:
        lt.append(i)
        lt.append("  ")
    dis = dis.join(lt)
    print(dis)
    print("\n")
    menu()
            
        

def menu():
    print("*"*20)
    print("Press any key to continue or press 1 to Exit.......")
    s = input()
    if s!="1":
        print("Guessing a Bollywood Movie Name................\n")
        play()


menu()
