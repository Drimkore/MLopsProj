FROM python:3.11
WORKDIR /app

EXPOSE 5000
COPY req.txt ./req.txt 
RUN pip install -r req.txt
COPY . .


CMD python main.py
CMD pytest tests.py
