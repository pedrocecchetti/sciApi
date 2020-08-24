FROM python:3

WORKDIR /app

ENV PYTHONPATH=.

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD [ "python", "./run.py" ]

COPY . .