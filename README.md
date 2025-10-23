# Lab 04

#### Argomenti

- Lettura su file (continuazione).
- Eccezioni (continuazione).
- Classi e oggetti (metodi dunder, getter e setter, collezioni di e relazioni tra oggetti).
- Ordinamento (di oggetti).
- Ereditarietà
- Polimorfismo

---

## Crociera

Il laboratorio prevede la progettazione di un sistema per la gestione delle prenotazioni delle cabine a 
bordo di una nave da crociera. La nave è identificata semplicemente da un nome e rappresenta l’elemento 
centrale attorno al quale ruota l’intero sistema. Al suo interno si trovano due insiemi principali: 
quello delle cabine, che possono avere caratteristiche diverse tra loro, e quello dei passeggeri, 
che rappresentano le persone registrate a bordo.
Tutte le informazioni necessarie per gestire il sistema sono raccolte in un unico file, denominato 
`dati_crociera.csv`. Questo file contiene sia i dati relativi alle cabine, sia quelli riguardanti i 
passeggeri. Ogni riga del file corrisponde a un elemento ben preciso: una cabina oppure un passeggero. 

Le righe dedicate alle cabine contengono sempre un codice univoco (ad esempio `CAB1`, `CAB2`, ..., `CABN`), 
seguito dal numero di letti presenti nella cabina, dal ponte in cui essa si trova e dal prezzo di base 
a notte. Alcune cabine, oltre alle informazioni di base, possono presentare delle caratteristiche 
aggiuntive che ne definiscono la tipologia. Se dopo il prezzo è presente un valore numerico, la riga 
fa riferimento a una cabina che consente di portare animali a bordo: il numero indicato rappresenta la 
quantità massima di animali ammessi. Se invece il valore aggiuntivo è una stringa di testo, la cabina è 
di tipo Deluxe e la stringa specifica lo stile, ad esempio `Moderna`, `Classica` o `Lussuosa`. 

Le righe relative ai passeggeri, invece, hanno una struttura più semplice: riportano un 
codice univoco che identifica il passeggero (ad esempio `P1`, `P2`,..., `PN`) e contengono il suo nome e cognome. 
Un possibile esempio del contenuto del file `dati_crociera.csv` è il seguente: 

```file
CAB1,2,3,120 
CAB2,3,5,200,Moderna 
P1,Marco,Rossi 
CAB3,2,2,140,2 
CAB4,4,6,300,Lussuosa 
...
```

### Prezzi delle cabine
Le cabine Standard sono le uniche per le quali il prezzo a notte corrisponde esattamente al valore 
indicato nel file. Per tutte le altre tipologie di cabina viene applicato un sovrapprezzo, calcolato 
in base alle loro caratteristiche: 

- Cabine con animali → sovrapprezzo pari al 10% per ogni animale ammesso, ovvero:
`prezzo finale = prezzo base × (1 + 0.10 × max_animali)`
- Cabine Deluxe → sovrapprezzo fisso del 20%: `prezzo finale = prezzo base × 1.20`

In questo modo, il costo finale delle cabine che ammettono animali cresce proporzionalmente al numero 
massimo di animali consentiti. 

### Implementazione
Per questo laboratorio è necessario utilizzare la classe `Crociera` presente nel 
file `crociera.py`. Le informazioni sulle cabine devono essere modellate tramite 
classi dedicate. Il file `main.py` consente di interagire con il sistema tramite 
un menù testuale utilizzabile dalla console. 

```menu in console
--- MENU CROCIERA ---
1. Modifica nome della crociera
2. Carica dati da file
3. Assegna cabina a passeggero
4. Visualizza cabine ordinate per prezzo
5. Visualizza elenco passeggeri
6. Esci
Scegli un'opzione >>
```

Le operazioni di gestione del sistema devono essere centralizzate all’interno della 
classe `Crociera`, che rappresenta l’elemento principale attraverso cui avviene 
ogni interazione con i dati. La modifica e la lettura delle informazioni relative 
alla nave, come ad esempio il nome, possono essere realizzate accedendo direttamente 
agli attributi della classe oppure, in modo più strutturato, tramite metodi getter 
e setter appositamente definiti. 

Uno dei compiti fondamentali della classe consiste nel caricamento dei dati dal 
file. A questo scopo deve essere implementato un metodo dedicato, 
`carica_file_dati(file_path)`, che si occupa di leggere il file e di creare in modo 
automatico gli oggetti corrispondenti alle righe presenti. In particolare, 
le righe relative alle cabine verranno interpretate per determinare la tipologia 
corretta, riflettendo e sfruttando l’aspetto dell’ereditarietà delle classi: se 
sono presenti solo quattro campi verrà creata una cabina Standard; se è presente un 
campo numerico aggiuntivo si tratterà di una cabina che ammette animali; infine, 
se il campo aggiuntivo è testuale verrà generata una cabina di tipo Deluxe).
Allo stesso modo, le righe relative ai passeggeri porteranno alla creazione degli 
oggetti specifici. Tutti questi oggetti verranno poi memorizzati all’interno del 
sistema per essere gestiti successivamente. Nel caso in cui il file non venga 
trovato, il metodo dovrà sollevare un’eccezione `FileNotFoundError` per segnalare 
l’errore. 

La classe `Crociera` deve prevedere inoltre un metodo per l’assegnazione di un 
passeggero a una cabina, chiamato 
`assegna_passeggero_a_cabina(codice_cabina, codice_passeggero)`. 
Quando viene effettuata una prenotazione, il sistema deve verificare che la cabina e 
il passeggero esistano, che la cabina sia effettivamente disponibile e che il 
passeggero non sia già associato a un’altra cabina. Se tutte le condizioni sono 
soddisfatte, la cabina viene contrassegnata come non disponibile e viene registrata 
l’associazione tra passeggero e cabina. Se una delle verifiche non va a buon fine, 
il metodo deve sollevare un’eccezione per segnalare l’errore.

Per facilitare la consultazione e la scelta delle cabine, la classe `Crociera` 
deve inoltre mettere a disposizione un metodo che permetta di visualizzare 
l’elenco delle cabine ordinate in base al prezzo a notte. 
Il metodo `cabine_ordinate_per_prezzo()` restituirà la lista delle cabine partendo 
da quelle più economiche fino a quelle più costose, fornendo così uno strumento 
utile sia per la gestione interna che per l’esperienza dell’utente.

Infine, la classe `Crociera` deve avere un metodo `elenca_passeggeri()` che stampa 
l’elenco dei passeggeri specificando, quando applicabile, la cabina a cui ciascun 
passeggero è associato. 

> **💡 NOTA:** 
> Per rendere le informazioni leggibili e chiare, tutte le classi coinvolte 
> devono implementare un metodo speciale di rappresentazione testuale, come 
> `__str__()` e/o `__repr__()`. In questo modo, quando un oggetto viene stampato, 
> restituirà una descrizione comprensibile e dettagliata del suo stato. Ad esempio, 
> la stampa di una cabina per animali potrebbe produrre un output come:
> 
> ```cabina stampata
> CAB6: Animali | 4 letti - Ponte 1 - Prezzo 234.00€ - Max animali: 3 – Disponibile
> ```
> Infine, implementare i metodi dunder `__eq__()` e/o `__lt__()` all’interno di una classe 
> quando è necessario definire la logica di uguaglianza (==) e/o di confronto 

> ordinato (<) tra istanze della classe.

