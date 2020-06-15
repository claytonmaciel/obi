#=========================#
# Questão Lingua_P        #
#=========================#


#forma 1
frase = input().strip()
frase = frase.replace("pppp","+") #quando tem 4 pppp é para ser substituído por dois pês
frase = frase.replace("ppp","-")
frase = frase.replace("p","")
frase = frase.replace("-","p")
frase = frase.replace("+","pp")
print(frase)

#forma 2
frase = input()
palavras = [palavra[1::2] for palavra in frase.split()]
print(' '.join(palavras))
