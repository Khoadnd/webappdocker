FROM python:3.10.8-alpine
COPY . /app
WORKDIR /app
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["rest.py"]
