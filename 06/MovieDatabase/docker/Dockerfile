FROM python:3.11
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /app
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]