FROM python:3.11
WORKDIR /app

EXPOSE 5000
COPY requirements.txt ./requirements.txt 
RUN pip install -r requirements.txt
COPY . .


CMD python main.py
CMD pytest tests.py
