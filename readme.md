# Interface d'analyse de sentiments

Ce dépôt contient une API HTTP et son interface homme-machine permettant d'analyser le sentiment dominant d'un texte (positif, négatif ou neutre). Il est également muni de fichiers de logs et d'une suite de tests sommaire.

## Installer le projet et ses dépendances

```bash
git clone https://github.com/Grouloo/module0-brief1.git

pip install -r requirements.txt

python -c "import nltk; nltk.download('vader_lexicon')"
```

## Démarrer

### Lancer le serveur HTTP

```bash
uvicorn main:app --host 0.0.0.0 --port 80
```

L'API sera ensuite disponible à l'adresse http://0.0.0.0/

### Lancer le frontend Streamlit

```bash
streamlit run sentiment_streamlit.py
```

Un nouvel onglet devrait s'ouvrir.

Si ce n'est pas le cas, l'application devrait tout de même être accessible depuis l'adresse http://localhost:8501/

### Lancer la suite de tests

```bash
pytest
```

## Endpoints

### Analyser un texte

```
POST /analyse_sentiment
```

#### Body

```json
{
  "text": "string"
}
```

#### Réponse

```json
{
  "raw": {
    "neg": "float",
    "neu": "float",
    "pos": "float",
    "compound": "float"
  },
  "interpretation": {
    "label": "string",
    "emoji": "string"
  }
}
```
