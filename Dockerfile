FROM python:3

# set a directory for the app
WORKDIR /flask

# copy all the files to the container
COPY . .
ENV PYTHONPATH=/flask/

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "app/__init__.py"]
