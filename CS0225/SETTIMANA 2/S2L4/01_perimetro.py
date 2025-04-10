# Scrivi un programma in python che in base alla scelta dell'utente permetta di calcolare il perimetro di diverse figure geometriche.


def perimetro():
        print("Inserisci la figura geometrica:")
        print("quadrato")
        print("pentagono")
        print("esagono")       
figura=input("Scegli la figura: ")
if figura=="quadrato":
      lato=float(input("Inserisci il valore del lato del QUADRATO: "))
      peri4=lato*4
      print(f"Il perimetro sarà: {peri4:.3f}")

elif figura=="pentagono":
    lato=float(input("Inserisci il valore del lato del PENTAGONO: "))
    peri5=lato*5
    print(f"Il perimetro sarà: {peri5:.3f}")
elif figura=="esagono":
    lato=float(input("Inserisci il valore del lato dell'ESAGONO: "))
    peri6=lato*6
    print(f"Il perimetro sarà: {peri6:.3f}")
else:
     print("Input non valido.")      