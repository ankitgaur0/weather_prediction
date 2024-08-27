FROM  python:3.9-slim-buster
WORKDIR /service

# the last . is used to use workdirectory
COPY Requirements.txt .
# . show the local directory and ./ represent the working directory(current directory)
COPY . ./


RUN pip install -r requirements.txt

ENTRYPOINT [ "python3","app.py" ]