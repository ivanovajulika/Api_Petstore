FROM python:3.10

WORKDIR /docker_workdir/

COPY requirements.txt ./docker_workdir/

RUN pip install --no-cache-dir -r ./docker_workdir/requirements.txt

COPY . ./docker_workdir/

CMD python -m pytest