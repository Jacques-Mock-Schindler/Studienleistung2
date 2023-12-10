---
title: "Studienleistung 2 Fachdidaktik 1 im GymInf-Programm im Herbstsemester 2023"
subtitle: "Konzeption einer Prüfungsaufgabe zu Funktionen in Python"
author: "Jacques Mock Schindler"
date: "10. Dezember 2023"
output: pdf_document
---

# Prüfungsaufgabe

Schreiben Sie eine Funktion, welche die Gesamtkapitalrentabilität einer
Investition (Return on Investment, RoI) aus den Grössen Ausgaben,
Einnahmen sowie investiertes Kapital berechnet.

Schreiben Sie für die Berechnung der RoI zwei Funktionen.

1. Eine Hilfsfunktion, welche den Gewinn der Investition berechnet.
2. Ein Hauptfunktion, welche unter Verwendung der Hilfsfunktion die RoI
   berechnet. Die RoI soll von der Funktion zurückgegeben werden.
   Ausserdem soll im Terminal "The RoI is 12.25%." mit dem korrekten RoI
   ausgegeben werden.

Versehen Sie Ihre Funktionen mit Type Hints und einem Docstring.


# Leitfragen

In diesem Text sollen die folgenden Fragen beantwortet werden:

>- Warum ist die Prüfungsaufgabe kognitiv anspruchsvoll?
>- Wie wird sichergestellt, dass die Lösung der Prüfungsaufgabe die
>  Erreichung bzw. Nicht-Erreichung des Lernziels tatsächlich beobachtbar
>  macht?
>- Welche Anhaltspunkte leiten die Korrektur dieser
>  Prüfungsaufgabe?

# Warum die Prüfungsaufgabe kognitiv anspruchsvoll ist

Die aktuelle Organisation des Unterrichts an Gymnasien ist in zweierlei
Hinsicht stark eingeschränkt. Einerseits orientiert sich der Unterricht
stark an den Fachdisziplinen. Andererseits stellt die
Organisation im Stundenplan mit der Taktung in 45 Minuten Einheiten eine
Einschränkung in zeitlicher Hinsicht dar.
Die zeitlichen Einschränkungen des Stundenplanes verhindern in vielen
Fällen interdisziplinäre Unterrichtseinheiten.
Diese beiden Einschränkungen führen in der Kombination zu einem
ausgeprägten Silo-Denken der Schülerinnen und Schüler (SuS).

Die gestellte Prüfungsaufgabe verlangt inhaltlich die Berechnung der
Gesamtkapitalrentabilität. Damit wird auf ein Inhalt aus dem Fach
Wirtschaft und Recht Bezug genommen. Dies zwingt die SuS, Wissen aus
einem Fach in einem anderen Fach anzuwenden. Ein solcher, wenn auch
bescheidener, interdisziplinärer Ansatz, stellt für viele SuS eine
Herausforderung dar und macht die Aufgabenstellung schon so
anspruchsvoll.

Die Aufgabenstellung für die Studienleistung 2 in der Fachdidaktik 1
verlangt explizit, dass die Prüfungsaufgabe die Definition einer
Funktion beinhalten muss. Das Programmieren von Funktionen ist per se
eine anspruchsvolle Aufgabe. Um entsprechende Probleme zu meistern, muss
die Aufgabenstellung zuerst in Teilprobleme zerlegt werden. Dies
entspricht Stufe 4 der Taxonomiestufen nach Bloom[^1]. 
Anschliessend müssen die Lösungen der Teilprobleme zu einer Gesamtlösung
zusammengefügt werden. Dies entspricht Stufe 5 der Taxonomiestufen nach
Bloom, wird diese doch umschrieben als "*Vorschläge zur Lösung konkreter
Problemstellungen entwickeln.*".

Damit erreicht die Aufgabenstellung immerhin die zweithöchste
Taxonomiestufe nach Bloom und darf als kognitiv anspruchsvoll bezeichnet
werden.

# Überprüfung der Lernziele

Der Prüfungsaufgabe liegen die folgenden Lernziele zugrunde:

>Die SuS
>
>- können Funktionen in Python definieren;
>
>- können selber definierte Funktionen in Scripts und als Bestandteil
>  eigener Funktionen verwenden und ausserdem
> 
>- können sie vordefinierte Funktionen in Scripts und als Bestandteil
>  eigener Funktionen verwenden.

Die Lernziele entsprechen im Wesentlichen jenen des Kapitel 7 aus dem
Lehrmittel Arnold et al., Informatik: Programmieren und Robotik:
Grundlagen der Informatik für Schweizer Maturitätsschulen. 1. Auflage,
Baar 2021.

Die Aufgabenstellung verlangt, dass zwei Funktionen durch die SuS
definiert werden. Auch wenn die SuS nur eine der beiden verlangten
Funktionen definieren, ist das erste Lernziel abgedeckt. Dadurch,
dass die Aufgabenstellung die Definition einer separaten Funktion zur
Berechnung des Gewinnes verlangt, ist auch sichergestellt, dass das
erste Lernziel überprüft werden kann, wenn die Aufgabe als ganzes nicht
gelöst wird.

Die Funktion zur Berechnung des Gewinnes stellt für sich alleine keine
besonders anspruchsvolle Aufgabe dar. Allerdings müssen die SuS die
selber definierte Hilfsfunktion in der ebenfalls selber zu definierenden
Hauptfunktion verwenden. Damit wird das zweite Lernziel abgedeckt.

Das
dritte Lernziel wird nicht explizit überprüft. Allerdings kann davon
ausgegangen werden, dass SuS, welche selber definierte Funktionen in
eigenen Funktionen verwenden, dies auch mit vordefinierten Funktionen
können. Implizit wird damit auch das dritte Lernziel überprüft.

So ist sichergestellt, dass durch die Prüfungsaufgabe alle drei
Lernziele überprüft werden.

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



[^1]: https://teachingtools.uzh.ch/asset/630f429c9b41e629750c95e2/download
    besucht am 10. Dezember 2023