FROM ubuntu:22.04 

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
    software-properties-common\
    sudo \
    curl \
    vim \
    unzip \
    rsync \
    build-essential \
    software-properties-common \
    ssh && \
  apt-get clean && \
  rm -rf /var/lib/apt/list/*


RUN apt-get update && apt-get install -y openjdk-11-jdk
## Download spark and hadoop dependencies and install

# Optional env variables
ENV SPARK_HOME=${SPARK_HOME:-"/opt/spark"}
ENV HADOOP_HOME=${HADOOP_HOME:-"/opt/hadoop"}

RUN mkdir -p ${HADOOP_HOME} && mkdir -p ${SPARK_HOME}
WORKDIR ${SPARK_HOME}

RUN curl https://downloads.apache.org/spark/spark-3.4.1/spark-3.4.1-bin-hadoop3.tgz -o spark-3.4.1-bin-hadoop3.tgz \
  && tar xvzf spark-3.4.1-bin-hadoop3.tgz --directory /opt/spark --strip-components 1 \
  && rm -rf spark-3.4.1-bin-hadoop3.tgz


RUN curl https://jdbc.postgresql.org/download/postgresql-42.6.0.jar -o \
  /opt/spark/jars/postgresql-42.6.0.jar


RUN apt-get update && apt-get install -y python3-pip
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PATH="/opt/spark/sbin:/opt/spark/bin:${PATH}"
ENV SPARK_HOME="/opt/spark"
ENV SPARK_MASTER="spark://spark-master:7077"
ENV SPARK_MASTER_HOST spark-master
ENV SPARK_MASTER_PORT 7077
ENV PYSPARK_PYTHON python3

COPY conf/spark-defaults.conf "$SPARK_HOME/conf"
COPY spark.py .

RUN chmod u+x /opt/spark/sbin/* && chmod u+x /opt/spark/bin/* 
ENV PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH

COPY entrypoint.sh .
RUN chmod u+x entrypoint.sh




ENTRYPOINT ["./entrypoint.sh"]
