FROM python:3.8-slim
WORKDIR /ols

COPY . /ols

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV NAME ols

CMD ["python", "./ols.py"]


