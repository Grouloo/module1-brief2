from fastapi import FastAPI
from pydantic import BaseModel
from nltk.sentiment import SentimentIntensityAnalyzer 
from loguru import logger
from sys import stderr
from interpret_sentiment import interpret_sentiment

sia = SentimentIntensityAnalyzer()
app = FastAPI()


logger.add(stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
logger.add("logs/sentiment_api.log")

logger.debug("L'API est en cours de démarrage...")


@app.get("/")
async def homepage():
    return {"message": "Hello World"}

class AnalyseSentimentInput(BaseModel):
    text: str

@app.post("/analyse_sentiment")
async def analyse_sentiment(input: AnalyseSentimentInput):
    logger.info(f"Analyse du texte: {input.text}")
    try:
        result = sia.polarity_scores(input.text)
        logger.info(f"Résultats: {result}")
        compound = result["compound"]
        label, emoji = interpret_sentiment(compound)
        return {
            "raw": {
                "neg": result["neg"],
                "neu": result["neu"],
                "pos": result["pos"],
                "compound": compound
            },
            "interpretation": {
                "label": label,
                "emoji": emoji  
            }  
        }
    except Exception as e:        
        logger.error(f"Erreur lors de l'analyse: {e}")        
        return {"error": str(e)}