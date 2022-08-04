def Countdown():
    Ctdown = list(range(10,-1,-1))
    String = "Launch in "
    for n in Ctdown:
        String+=str(n)
        if n > 0:
            String+="..."
    return Ctdown, String
    
print(Countdown())