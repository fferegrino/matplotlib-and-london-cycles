FROM python:3.9.15

WORKDIR /app

RUN git clone --depth 1 https://github.com/fferegrino/london-cycles-db.git

RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  libatlas-base-dev \
  libgdal-dev \
  gfortran

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY *.py ./

ENTRYPOINT ["python","./app.py"]
