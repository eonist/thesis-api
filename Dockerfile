FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /api
COPY ./requirements.txt /api/requirements.txt
RUN pip install -r requirements.txt
COPY . /api
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]