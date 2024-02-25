
FROM amazon/aws-lambda-python:3.9

COPY ./requirements.txt /requirements.txt
RUN yum -y install gcc-c++
RUN pip install --no-cache-dir torch --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir -r /requirements.txt


RUN mkdir -p /tmp/cache
RUN mkdir -p /tmp/cache/easynmt
RUN mkdir -p /tmp/huggingface/transformers
RUN mkdir -p /tmp/cache/torch
RUN mkdir -p /tmp/nltk_data

RUN chmod -R 722 /tmp/huggingface/transformers
RUN chmod -R 722 /tmp/cache
RUN chmod -R 722 /tmp/cache/easynmt
RUN chmod -R 722 /tmp/cache/torch
RUN chmod -R 722 /tmp/nltk_data

ENV NLTK_DATA=/tmp/nltk_data
ENV EASYNMT_CACHE=/tmp/cache/easynmt
ENV TRANSFORMERS_CACHE=/tmp/cache/transformers
ENV TORCH_CACHE=/tmp/cache/torch

COPY handler.py ${LAMBDA_TASK_ROOT}

CMD [ "handler.main" ]

