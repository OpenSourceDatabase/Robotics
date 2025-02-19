FROM python:3.10

RUN python -m pip install Django django-publications 

RUN git clone https://github.com/OpenSourceDatabase/Robotics.git

WORKDIR Robotics/publication-server

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

