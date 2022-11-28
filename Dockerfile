FROM python:3.9.15

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  libatlas-base-dev \
  libgdal-dev \
  gfortran

COPY requirements.txt requirements-plot.txt ./

RUN pip install -r requirements.txt && \
    pip install -r requirements-plot.txt

COPY *.py ./
COPY data/ ./data/
COPY shapefiles ./shapefiles/

ENTRYPOINT ["python", "./app.py"]
