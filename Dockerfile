FROM python:3.7

ADD requirements.txt .

RUN pip install -r requirements.txt

RUN python -m nltk.downloader all

ADD . /code

WORKDIR /code

#RUN pytest

ENTRYPOINT [ "python", "app.py" ]

