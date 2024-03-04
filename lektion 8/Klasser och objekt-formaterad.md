## Klasser & Objekt! 

| Nomenklatur<br>(vad man menar med en specifik fras eller ord) |                                                                                                                                                                                                                 |
|---------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Objektorienterad<br/>programmering                            | En typ av programmering där man använder sig av objekt för att dela upp data och funktioner.<br/>Inkapsling är en av de viktigaste bitarna och vi känner till det begreppet sen tidigare med namnet namespaces. |
| Objekt                                                        | En grupp data och instruktionerna för datorn om hur man behandlar sagda data.<br/>En Instans av en Klass.                                                                                                       |
| Instans                                                       | En specifik kopia av ett koncept.<br/>T.ex. en specifik bok istället för konceptet böcker.                                                                                                                      |
| Klass                                                         | En ritning för en typ av objekt.                                                                                                                                                                                |
| Metoder                                                       | Funktioner som ligger i ett objekt. \(Eller en Klass men det är utanför grundkursen\)<br/>Har alltid argumentet self i de situationer vi går igenom på grundkursen.                                             |
| Attribut                                                      | Egenskaper hos objekt. Oftast data/variabler och metoder.                                                                                                                                                       |
| Konstruktor                                                   | \_\_init\_\_-metoden som körs när man skapar ett objekt.                                                                                                                                                        |
| Arv                                                           | När man använder sig av en annan ritning \(en annan klass\) för att påbörja ritningen för en ny klass.                                                                                                          |

Exempelstruktur:

    Klass = Bok
    Klass som ärver från Bok = Pocketbok(Bok)
    Klass som ärver från Pocketbok = SaganOmRingenSomPocket(Pocketbok, SaganOmRingen)
    Objekt skapat från klassen SaganOmRingenSomPocket = Mitt exemplar av den boken.