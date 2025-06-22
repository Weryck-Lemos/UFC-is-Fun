def palindromo(txt):
    for i in range(n):
        if( txt[i] != txt[n-i-1]):
            return False
        
    return True

txt = input()
txt =  txt.replace(" ","").replace(",", "").replace(".","").replace("!","").replace("?","")
txt = txt.lower()

n = len(txt)
if palindromo(txt):
    print("SIM")

else:
    print("NAO")
