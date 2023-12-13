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
Einnahmen sowie dem investierten Kapital berechnet.

Implementieren Sie im beiliegenden File `aufgabe.py` die beiden Funktionen

1. `_earnings()`, welche den Gewinn der Investition berechnet sowie
2. `return_on_investment()`, welche unter Verwendung der Funktion
   `_earnings()` die RoI berechnet. Die RoI soll von der Funktion
   zurückgegeben werden. Ausserdem soll im Terminal "The RoI is 12.25%."
   mit dem korrekten RoI ausgegeben werden.

Versehen Sie Ihre Funktionen mit Type Hints und einem Docstring.

Das File für Abgabe wird mit den Signaturen der beiden verlangten
Funktionen zur Verfügung gestellt. In den Signaturen fehlen aufgrund der
konkreten Aufgabenstellung die Type Hints.


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
Hauptfunktion verwenden. Aufgrund der Aufgabenstellung ist damit zu
rechnen, dass einzelne SuS Redundanzen schaffen werden und die Logik für
die Berechnung des Gewinnes entgegen der Aufgabenstellung direkt in in
der Funktion `return_on_investment()` implementieren werden.

Das zweite Lernziel wird nur erfüllt, wenn die Funktion `_earnings()` in
für die Berechnung der RoI verwendet wird. Anspruchsvoll ist dieser Teil
der Aufgabe weil die Lösung in Teilschritten zu erfolgen hat.

Das
dritte Lernziel wird nicht explizit überprüft. Allerdings kann davon
ausgegangen werden, dass SuS, welche selber definierte Funktionen in
eigenen Funktionen verwenden, auch in der Lage sind, vordefinierte
Funktionen zu verwenden. Implizit wird damit auch das dritte Lernziel
überprüft.

So ist sichergestellt, dass durch die Prüfungsaufgabe alle drei
Lernziele überprüft werden.

## Korrekturanleitung

Der Korrektur liegt folgendes Punkteschema zu Grunde:

Für die

- Implementierung der Hilfsfunktion gibt es 1 Punkt;
- die Type Hints und den Docstring der Hilfsfunktion gibt es 1 Punkt;
- die korrekte Implementierung der Berechnung der RoI gibt 1 Punkt;
- die Ausgabe im Terminal gibt 1 Punkt sowie
- die korrekte Formatierung des Resultates im Terminal gibt 1 Punkt.

Die gesamte Aufgabe gibt damit 5 Punkte.

Da gemäss Ausgangslage die Prüfungsaufgabe für die ganze Fachschaft zur
Verfügung gestellt wird, wird die Prüfung von einer Vielzahl von SuS
abgelegt.
Entsprechend wichtig ist es, dass bereits beim Erstellen der
Prüfungsaufgabe der Aufwand für die Korrektur mitberücksichtigt wird.
Wenn die Aufgabenstellung wie im vorliegenden Fall ganze Funktionen als
Lösung erfordert, kann für die Korrektur auf die von Python zur
Verfügung gestellten Unittests abgestellt werden. So kann die Korrektur
- zumindest für die korrekten Lösungen - für die Logik, die Formatierung
der Ausgabe sowie die Type Hints automatisiert werden.

Da die verlangten Docstrings individuell ausgestaltet formuliert werden
können, können diese nicht automatisiert korrigiert werden und müssen
manuell im Code der Abgabe korrigiert werden.

Entsprechend umfasst die Abgabe neben dem File für die Abgabe der
Antwort und der Musterlösung auch noch ein File mit dem Unittest für die
Überprüfung der Funktionsfähigkeit der Schülerlösungen.


[^1]: https://teachingtools.uzh.ch/asset/630f429c9b41e629750c95e2/download
    besucht am 10. Dezember 2023