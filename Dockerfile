FROM python:3

ENV PYTHONPATH=.
RUN pip install pipenv
WORKDIR /app

COPY Pipfile .

RUN pipenv lock --requirements > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "./run.py" ]