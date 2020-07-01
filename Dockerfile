FROM python:3.7.5-alpine
COPY requirements.txt /
RUN python -m pip install -r requirements.txt
ADD app.py /
ADD setup.py /
CMD [ "python", "./app.py" ]
EXPOSE 5000

