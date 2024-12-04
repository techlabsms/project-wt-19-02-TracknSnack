#Programm zur Umrechnung
a="kg" or "Kilogramm" or "kilogram"
b="mg" or "Milligramm" or "milligram"
c="l" or "Liter"
d="Esslöffel" or "EL" or "tbsp" or "tablespoon"
e="Teelöffel" or "TL" or "tsp" or "teaspoon"
f="Messerspitze" or "Msp"
g= "pound" or "pd" or "pounds"
h= "ounce" or "ounces"

print ("Dies ist ein Programm zur Umrechnung von Einheiten")
print ("Geben Sie die Einheit, die Sie gegeben haben ein: ")
eingabe1=input()
print ("Geben Sie den Wert an: ")
wert = float (input())

if eingabe1 == a:
    (g) = wert / 1000
    print ("g: ", wert)

if eingabe1 == b:
    (g) = wert * 1000
    print ("g: ", wert)

if eingabe1 == c:
    (ml) = wert * 1000
    print ("ml ", wert)

if eingabe1 == d:
    (ml) = wert * 15
    print ("ml: ", wert)

if eingabe1 == e:
    (ml) = wert * 5
    print ("ml: ", wert)

if eingabe1 == f:
    (g)= wert * 3/10
    print ("g:", wert)

if eingabe1 ==g:
    (g)= wert * 454
    print ("g:", wert)

if eingabe1 == h:
    (g)= wert * 28.35
    print ("g:", wert)