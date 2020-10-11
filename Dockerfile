FROM python:3.6
COPY requirements.txt /code/requirements.txt
WORKDIR /code
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "app.py"]