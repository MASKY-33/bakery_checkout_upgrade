def bedrag():
    prijs = float(input("Product prijs: "))
    product_naam = input("Productnaam: ")
    hoeveelheid = int(input("Product hoeveelheid: "))


    totaal_bedrag = totaal(prijs, hoeveelheid)

    print(f"Klant heeft {hoeveelheid}x van {product_naam}. Bedrag te betalen, €{totaal_bedrag:.2f}")



def totaal(prijs, hoeveelheid):
    if hoeveelheid >= 5:
        return prijs * hoeveelheid - (prijs * hoeveelheid) * 0.10 # <-- Eerst; 'prijs * hoeveelheid' vooraan de (-), 2de; '(prijs * hoeveelheid) * 0,10', 3de; 'prijs * hoeveelheid vooraan de (-)' met de uitkomst van (prijs * hoeveelheid) * 0.10
    else:
        return prijs * hoeveelheid


bedrag()
