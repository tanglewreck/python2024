# Variabler och Datatyper

## Ordet variabel kommer från att de är variabla värden.

Variabler är saker vi sparar i datorns minne.  
Datatyper är HUR vi sparar data.

`Syntax = Grammatik`


### Typer av datatyper:

Vissa Datatyper kan bara innehålla en specifik typ av sak. Jag kallar dessa för "**simpla datatyper**".  
**Samlingsdatatyper**, datatyper som kan innehålla flera saker.

`Varje sak som ligger i en variabel av en samlingsdatatyp kallas för Element.`


### Datatyper som bara kan innehålla en typ av sak ("simpla datatyper")
| Internt namn | Betydelse | Exempel |
| :--- | :--- | :--- |
| str | String = Text | Ex: "Hej, hallå!", 'Hej, Hallå!', """Hej, Hallå!""" |
| int | Integer = Heltal | Ex: 2 |
| float | Float = Flyttal/Decimaltal | Ex: 2.0 |
| bool | Boolean = Sant/Falskt | False, True |


### Samlingsdatatyper
| Internt namn | Betydelse | Metafor/Beskrivning | Exempel                                                                    |
|:-------------| :--- | :--- |:---------------------------------------------------------------------------|
| list         | List = Lista | Kan ses på som en hylla, allt står i en viss ordning. | \[1, 2, 3\]                                                                |
| tuple        | Tuple | Kan ses på som en hylla där någon har superlimmat fast allting. | \(1, 2, 3\)                                                                |
| dict         | Dictionary = Ordbok | Kan ses på som en faktisk ordbok, man slår upp betydelser av ord. Alla element är i formatet nyckel:värde. | {2:"två", "ålder":33}<br>johan = {"namn":"Johan", "ålder":34, "längd":180} |
| set          | Set = Mängd | Kan ses på som en låda där det bara får finnas en av varje sak. Det som läggs i lådan får inte kunna ändras på. | {1, 2, 3}                                                                  |


#### Nedanstående är en referens för snabb översikt:
* list skapas med []
* tuple skapas med ()
* dict skapas med {} och måste vara i nyckel:värde-format
* set skapas med {} Se nedan för ett förtydligande!

När man skapar samlingsvariabler så kan de vara tomma, t.ex. `a = ()`, men det finns ett viktigt undantag:
För att skapa ett tomt set så kan man inte skriva `a = {}`, då blir det ett tomt dictionary. Vad man
måste göra är att skriva `a = set()`, då blir det ett tomt set.


##### **Konkatenering** är att slå ihop två saker, t.ex. strängar, genom att lägga dem efter varandra.
