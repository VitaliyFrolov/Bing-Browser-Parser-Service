FROM mirror.gcr.io/library/python:3.12-slim as builder

WORKDIR /bing-browser-parser-api

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libffi-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM mirror.gcr.io/library/python:3.12-slim

WORKDIR /bing-browser-parser-api

COPY --from=builder /install /usr/local
COPY . .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload" ]