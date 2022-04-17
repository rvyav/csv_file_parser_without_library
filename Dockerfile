FROM python:3.8

# set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

COPY . /app/

# using `&&` make it faster
# instead of using multiple `RUN` directives
RUN pip install -r requirements.txt && \
    pip install --upgrade pip

CMD ["python3", "./app/app.py"]
