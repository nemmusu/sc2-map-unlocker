# Readme
[README: Italiano](./README_IT.md)

[README: English](./README.md)

# Tabella dei contenuti

- [Readme](#readme)
- [Stronghold Crusader 2 Map Unlocker](#stronghold-crusader-2-map-unlocker)
- [Eseguibile](#eseguibile)
- [Per utilizzare lo script installare PyQt5 utilizzando pip](#per-utilizzare-lo-script-installare-pyqt5-utilizzando-pip)
- [Compilazione](#compilazione)
- [Screenshot](#screenshot)

# Stronghold Crusader 2 Map Unlocker

Questo è un semplice programma che consente di sbloccare le mappe originali di Stronghold Crusader 2 in modo che possano essere modificate dall'editor di mappe.

Il programma è stato creato utilizzando il linguaggio di programmazione Python e la libreria PyQt5 per l'interfaccia grafica.

Per utilizzare il programma, è possibile eseguire il file unlocker.exe incluso nell'archivio `stronghold_map_unlocker.zip`. Per creare questo file .exe, è stato utilizzato il comando `python compile.py build` (il file `compile.py` è presente nel repository).

Una volta avviato il programma, per sbloccare una mappa, fare clic sul pulsante "Sblocca Mappe". Verrà richiesto di selezionare il file .shmap da sbloccare. Una volta selezionato il file, verrà creato un nuovo file con estensione "-unlocked.shmap" che conterrà la mappa sbloccata, verrà chiesto dove salvare il file.La mappa si chiamerà con il nome del file e sarà possibile modificare la descrizione dal map editor.

Una volta completata l'operazione, verrà visualizzato un messaggio di conferma.

# Eseguibile

Nella cartella `build` è presente un file zip che contiene una versione eseguibile del programma (già compilata e pronta all uso).

# Per utilizzare lo script installare PyQt5 utilizzando pip
Puoi eseguire il seguente comando nel tuo terminale:

```
pip install pyqt5
```

Per avviare lo script `map_unlocker.pyw`, segui questi passaggi:

1. Assicurati di aver installato PyQt5 come descritto sopra.

2. Apri il tuo terminale e spostati nella directory in cui si trova il file `map_unlocker.pyw`.

3. Esegui il comando seguente per avviare lo script:

```
python map_unlocker.pyw
```

Lo script aprirà una finestra con l'interfaccia grafica del programma Stronghold Crusader 2 Editor Unlocker. Puoi quindi utilizzare il programma per sbloccare le mappe come descritto nella descrizione sopra.

# Compilazione
Per creare l'eseguibile del programma Stronghold Crusader 2 Editor Unlocker, è necessario utilizzare cx_Freeze, un modulo Python che consente di creare pacchetti eseguibili a partire da script Python.

Prima di tutto, è necessario installare cx_Freeze utilizzando pip. Puoi eseguire il seguente comando nel tuo terminale:

```
pip install cx_Freeze
```

Una volta installato cx_Freeze, puoi procedere con la creazione dell'eseguibile del programma.
Esegui il seguente comando per creare l'eseguibile:

```
python compile.py build
```

Questo comando utilizzerà cx_Freeze per creare l'eseguibile del programma. L'eseguibile verrà creato nella directory `build` all'interno della directory corrente.

Una volta completata la creazione dell'eseguibile, puoi eseguirlo semplicemente facendo doppio clic sul file `unlocker.exe`.

# Screenshot

![SC2 Map Unlocker](https://github.com/nemmusu/sc2-map-unlocker/blob/main/screenshots/interface_example.png)


