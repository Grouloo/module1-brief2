FROM python:3.12.12-slim-trixie

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN chmod +x start.sh

EXPOSE 8000
EXPOSE 8080

CMD ["./start.sh"]