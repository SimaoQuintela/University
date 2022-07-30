def diferentes(frases):
    
    r = []
    for frase in frases:
        difs = len(list(set(frase)))
        r.append((frase,difs))
    
    r.sort(key= lambda x: (-x[1],x[0]))
    
    r2 = [ x[0] for x in r]
    
    
    return r2