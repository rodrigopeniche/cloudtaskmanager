FROM python:2.7

COPY . /backend

WORKDIR /backend

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]