# Konzeption einer Prüfungsaufgabe zu Funktionen in Python

In diesem Text sollen die folgenden Fragen beantwortet werden:

- Warum ist die Prüfungsaufgabe kognitiv anspruchsvoll?
- Wie stelle ich sicher, dass die Lösung der Prüfungsaufgabe die
  Erreichung bzw. NichtErreichung des Lernziels tatsächlich beobachtbar
  macht?
- Welche Anhaltspunkte werden mich in der Korrektur dieser
  Prüfungsaufgabe leiten?

## Aufgabenstellung

a. Schreiben Sie eine Funktion
   `zwischenergebnis(wert_des_zwischenergebnisses)`, welche ein Parameter
   entgegennimmt und diesen in der Form *Zwischenergebnis:
   wert_des_zwischenergebnises* am Bildschirm ausgibt.

   ```Python
   def zwischenergebnis(wert_des_zwischenergebnises):
       print (f'Zwischenergebnis: {wert_des_zwischenergebnises}')
   ```

b. Schreiben Sie eine Funktion `ringflaeche(r_g,
r_k)`, welche zwei Radien entgegennimmt und aus diesen die
Fläche des dadurch definierten Ringes berechnet. Darüber hinaus soll die
Funktion unter Verwendung der von Ihnen in Teilaufgabe a. geschriebenen
Funktion die Flächen der beiden den Ring definierenden Kreise ausgeben
(Falls Sie Teilaufgabe a. nicht gelöst haben, verzichten Sie auf die
Ausgabe der Zwischenresultate).

Zur Erinnerung: Die Fläche eines Kreises berechnet sich nach der Formel
$A = \pi \cdot r^2$. $\pi$ kann als 3.14 angenommen werden.

```Python
def ringflaeche(r_g, r_k):
    PI = 3.14

    akg = PI * r_g ** 2
    zwischenergebnis(akg)

    akk = PI * r_k ** 2
    zwischenergebnis(akk)
    
    return akg - akk
```