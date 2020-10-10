FROM python:3.6
COPY requirements.txt /code/requirements.txt
ENV HTTP_PROXY="http://proxy.cs.ui.ac.id:8080"
ENV HTTP_PROXY="http://proxy.cs.ui.ac.id:8080""
WORKDIR /code
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "app.py"]