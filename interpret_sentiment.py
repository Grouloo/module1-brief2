def interpret_sentiment(compound: float):
    if compound > 0.05:
        return "Positif", "😊"
    elif compound < -0.05:
        return "Négatif", "😢"
    else:
        return "Neutre", "😐"