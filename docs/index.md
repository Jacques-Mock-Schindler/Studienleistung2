---
title: "Studienleistung 2 Fachdidaktik 1 im GymInf-Programm im Herbstsemester 2023"
author: "Jacques Mock Schindler"
date: "10. Dezember 2023"
output: pdf_document
---

# Konzeption einer Prüfungsaufgabe zu Funktionen in Python

## Aufgabenstellung

Schreiben Sie eine Funktion, welche die Gesamtkapitalrentabilität einer
Investition (Return on Investment, RoI) berechnet.

Schreiben Sie für die Berechnung der RoI zwei Funktionen.

1. Eine Hilfsfunktion, welche den Gewinn der Investition berechnet.
2. Ein Hauptfunktion, welche unter Verwendung der Hilfsfunktion die RoI
   berechnet. Die RoI soll von der Funktion zurückgegeben werden.
   Ausserdem soll im Terminal "The RoI is 12.25%." mit dem korrekten RoI
   ausgegeben werden.

Versehen Sie Ihre Funktionen mit Type Hints und einem Docstring.

Schreiben Sie eine Funktion, welche die Differenz zwischen zwei Zahlen
berechnet. Die Differenz soll immer eine positive Zahl sein. Um dies
sicherzustellen, soll die Funktion für die Berechnung unabhängig von der
Benutzereingabe die kleiner Zahl von der grösseren abziehen.

Schreiben Sie für die Lösung dieses Problems zwei Funktionen

a. eine Hilfsfunktion, welche sicherstellt, dass in der Rechnung $a - b$ $b$
   nicht grösser ist als $a$ und
b. eine Hauptfunktion, welche die Differenz berechnet und zurück gibt.

Versehen Sie Ihre Funktionen mit Type Hints und einem Docstring.

## Leitfragen

In diesem Text sollen die folgenden Fragen beantwortet werden:

>- Warum ist die Prüfungsaufgabe kognitiv anspruchsvoll?
>- Wie wird sichergestellt, dass die Lösung der Prüfungsaufgabe die
>  Erreichung bzw. Nicht-Erreichung des Lernziels tatsächlich beobachtbar
>  macht?
>- Welche Anhaltspunkte leiten die Korrektur dieser
>  Prüfungsaufgabe?

## Warum die Prüfungsaufgabe kognitiv anspruchsvoll ist

Die aktuelle Organisation des Unterrichts an Gymnasien ist in zweierlei
Hinsicht stark eingeschränkt. Einerseits orientiert sich der Unterricht
stark an den Fachdisziplinen, was bei den Schülerinnen und Schülern
(SuS) zu einem ausgeprägten Silo-Denken führt. Andererseits stellt die
Organisation im Stundenplan mit der Taktung in 45 Minuten Einheiten eine
Einschränkung in zeitlicher Hinsicht dar.

Die gestellte Prüfungsaufgabe verlangt inhaltlich die Berechnung der
Gesamtkapitalrentabilität. Damit wird auf ein Inhalt aus dem Fach
Wirtschaft und Recht Bezug genommen. Dies zwingt die SuS, Wissen aus
einem Fach in einem anderen Fach zu verwenden. Ein solcher, wenn auch
bescheidener, interdisziplinärer Ansatz stellt für viele SuS eine
Herausforderung dar.

Wenn eine Funktion zu Programmieren ist, muss die Aufgabenstellung in
Teilprobleme zerlegt werden. Die Lösungen der Teilprobleme müssen
anschliessend zu einem neuen Ganzen zusammengefügt werden. Damit
entspricht die Aufgabe der Stufe 5 - Synthese - der
Bloomschen Taxonomiestufen[^1].

## Überprüfung der Lernziele

Der Prüfungsaufgabe liegen die folgenden Lernziele zugrunde:

>Die SuS
>- können Funktionen in Python definieren;
>- können selber definierte Funktionen in Scripts und als Bestandteil
>  eigener Funktionen verwenden ausserdem
>- können sie vordefinierte Funktionen in Scripts und als Bestandteil
>  eigener Funktionen verwenden.

Die Aufgabenstellung verlangt, dass zwei Funktionen durch die SuS
definiert werden. Dabei soll eine der beiden Funktionen die andere
verwenden. Damit werden die ersten beiden Lernziele überprüft. Das
dritte Lernziel wird nicht explizit überprüft. Allerdings kann davon
ausgegangen werden, dass SuS, welche selber definierte Funktionen in
eigenen Funktionen verwenden, dies auch mit vordefinierten Funktionen
können. Implizit wird damit auch das dritte Lernziel überprüft.

## Korrekturanleitung

Für die

- Implementierung der Hilfsfunktion gibt es 1 Punkt;
- die Type Hints und den Docstring der Hilfsfunktion gibt es 1 Punkt;
- die korrekte Implementierung der Berechnung der RoI gibt 1 Punkt;
- die Ausgabe im Terminal gibt 1 Punkt sowie
- die korrekte Formatierung des Resultates im Terminal gibt 1 Punkt.

Die gesamte Aufgabe gibt damit 5 Punkte.

Die Logik und die Ausgabe kann mit Hilfe des Unittests überprüft werden.
Manuell zu korrigieren bleiben die Type Hints und Docstrings. Ausserdem
muss bei fehlerhaftem Unittest der Code für die Vergabe von Teilpunkten
manuell geprüft werden.



[^1]: https://paeda-logics.ch/wp-content/uploads/2020/01/Taxonomiestufen_Bloom.pdf
    besucht am 8. Dezember 2023