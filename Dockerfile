FROM python:3

ENV PYTHONPATH=.

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["pipenv", "run", "python", "./run.py" ]