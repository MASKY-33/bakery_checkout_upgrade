def bedrag():
    prijs = float(input("Product prijs: "))
    product_naam = input("Productnaam: ")
    aantal = int(input("Product hoeveelheid: "))


    totaal_bedrag = totaal(prijs, aantal)

    print(f"Klant heeft {aantal}x van {product_naam}. Bedrag te betalen, €{totaal_bedrag:.2f}")



def totaal(prijs, aantal):
    if aantal >= 5:
        return prijs * aantal - (prijs * aantal) * 0.10 # <-- Eerst; 'prijs * aantal' vooraan de (-), 2de; '(prijs * aantal) * 0,10', 3de; 'prijs * aantal vooraan de (-)' met de uitkomst van (prijs * aantal) * 0.10
    else:
        return prijs * aantal


bedrag()
