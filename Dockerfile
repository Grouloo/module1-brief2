FROM python:3.12.12-slim-trixie

WORKDIR /app

COPY . .

# Installation des dépendances
RUN pip install -r requirements.txt
RUN python -c "import nltk; nltk.download('vader_lexicon')"

# Tests
RUN pytest

RUN chmod +x start.sh

EXPOSE 8000
EXPOSE 8080

CMD ["./start.sh"]