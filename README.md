# WZ Audio Manager

WZ Audio Manager è un widget sempre visibile, sopra ogni applicazione, che consente di gestire l'audio del gioco, la chat e il microfono di Discord, fornendo un feedback visivo sullo stato di ciascun elemento.

## Come Eseguirlo

Per eseguire il widget, basta avviare il file `wzaudiomanager.exe` situato nella cartella *'ESEGUIBILE'*. Per il corretto funzionamento, è necessario solo il file eseguibile e il file `config.ini`, che deve essere sempre nella stessa cartella dell'eseguibile. I file presenti nella cartella *'repos'* appartengono al progetto e non sono necessari per l'esecuzione del programma.

## Come Usarlo

Nel widget sono presenti i seguenti elementi:

- **Icona a sinistra**: consente di trascinare il widget sullo schermo.
- **Primo bottone**: attiva o disattiva il microfono.
- **Secondo bottone**: silenzia o riattiva l'audio della chat.
- **Terzo bottone**: silenzia o riattiva l'audio del gioco.
- **Quarto bottone**: silenzia o riattiva sia l'audio della chat che del gioco.
- **Icona di chiusura**: consente di chiudere il widget.

Accanto a ciascuno dei tre bottoni principali è presente un semaforo che indica lo stato del microfono, dell'audio della chat e dell'audio di gioco. Ogni semaforo può essere cliccato per sincronizzare manualmente lo stato con quello effettivo, nel caso non sia allineato.

## Come Configurarlo

Prima di avviare l'eseguibile, è necessario modificare il file `config.ini` (aperto con il Blocco Note o un editor di testo). All'interno del file, è possibile configurare le combinazioni di tasti assegnate ai tre bottoni del widget. Le combinazioni devono essere modificate in base a quelle configurate in Discord (in *Impostazioni Discord* → *Associazioni tasti*). Le combinazioni da modificare sono le seguenti:
```ini
# COMBINAZIONE SILENZIA MICROFONO
combination1 = ctrl, m

# COMBINAZIONE SILENZIA CHAT
combination2 = ctrl, d

# COMBINAZIONE SILENZIA GIOCO
combination3 = f10
```

Scrivere le combinazioni che avete configurato in Discord per attivare/disattivare il microfono e per silenziare/riattivare l'audio rispettivamente in combination1 e combination2.

Una volta modificate, salvare il file config.ini e avviare l'eseguibile.

Nel file config.ini sono anche presenti altri parametri configurabili che influenzano lo stile e il comportamento del widget. Se il parametro discord_logic è impostato su false, i tasti per il microfono e la chat agiscono in maniera indipendente.

## MIT License

Copyright (c) 2024 albste

Con la presente si concede gratuitamente a chiunque ottenga una copia di questo software e dei relativi file di documentazione (il "Software"), di utilizzarlo, copiare, modificare, fondere, pubblicare, distribuire, sublicenziare e/o vendere copie del Software, e di consentire alle persone a cui il Software è fornito di fare altrettanto, nelle seguenti condizioni:

La presente avvertenza di copyright e questa dichiarazione di permesso devono essere incluse in tutte le copie o porzioni sostanziali del Software.

IL SOFTWARE È FORNITO "COSÌ COM'È", SENZA GARANZIE DI NESSUN TIPO, ESPRESSE O IMPLICITE, INCLUSE MA NON LIMITATE A GARANZIE DI COMMERCIABILITÀ, IDONEITÀ PER UN FINE PARTICOLARE E NON VIOLAZIONE. IN NESSUN CASO GLI AUTORI O I DETENTORI DEL COPYRIGHT POTRANNO ESSERE RITENUTI RESPONSABILI PER QUALSIASI DANNO, ANCHE SE CONSAPEVOLE DELLA POSSIBILITÀ DI TALE DANNI, DERIVANTE DA O IN CONNESSIONE CON L'USO DEL SOFTWARE.