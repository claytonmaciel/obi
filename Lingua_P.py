frase = input().strip()
frase = frase.replace("pppp","+") #quando tem 4 pppp é para ser substituído por dois pês
frase = frase.replace("ppp","-")
frase = frase.replace("p","")
frase = frase.replace("-","p")
frase = frase.replace("+","pp")
print(frase)