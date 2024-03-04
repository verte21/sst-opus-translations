FROM amazon/aws-lambda-python:3.9

COPY ./requirements.txt .

RUN yum -y install gcc-c++
RUN pip install --no-cache-dir torch --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir -r requirements.txt

ENV HOME /tmp

COPY handler.py ${LAMBDA_TASK_ROOT}

CMD ["handler.main"]

