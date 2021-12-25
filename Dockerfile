FROM python

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN python -m spacy download en_core_web_lg && python -m spacy link en_core_web_lg es
COPY . /app
CMD ["python3", "-m", "src.app"]