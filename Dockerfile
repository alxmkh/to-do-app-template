FROM python:3.10-alpine

RUN mkdir -p /backend && /usr/local/bin/python -m pip install --upgrade pip && pip install pipenv

ENV PROJECT_DIR /backend

ENV PORT 3001

WORKDIR ${PROJECT_DIR}

COPY Pipfile* ${PROJECT_DIR}/

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pipenv install --deploy --system \
    && apk del build-deps

COPY . ${PROJECT_DIR}

RUN cd ${PROJECT_DIR}

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "3001"]
