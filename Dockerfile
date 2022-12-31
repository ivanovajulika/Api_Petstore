FROM python
WORKDIR /tests/
COPY requirements.txt .
RUN pip install -r requairements.txt
CMD pytest