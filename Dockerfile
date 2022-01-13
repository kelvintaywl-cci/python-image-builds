FROM python:3.7

RUN pip3 install --upgrade pip \
    && pip3 install --no-cache-dir numpy==1.20.3 \
    && pip3 install --no-cache-dir spacy==3.0.5 \
    && pip3 install --no-cache-dir scipy==1.6.3 \
    && pip3 install --no-cache-dir cython==0.29.23 \
    && pip3 install --no-cache-dir scikit-learn==0.24.2 \
    && pip3 install --no-cache-dir nltk==3.6.2

RUN pip3 install --no-cache-dir awscli \
    && python -m spacy download en_core_web_md \
    && python -m spacy download en_core_web_sm \
    && python -m spacy download zh_core_web_md
