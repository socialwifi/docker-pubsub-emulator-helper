FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN pip install --no-cache-dir pip==8.1.2
RUN mkdir /package
WORKDIR /package

ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1

RUN apt-get update && \
    apt-get install -yqq curl \
        openjdk-8-jre && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN \
    curl https://sdk.cloud.google.com | bash && \
    /root/google-cloud-sdk/bin/gcloud components install -q pubsub-emulator beta && \
    /root/google-cloud-sdk/bin/gcloud components update -q pubsub-emulator beta

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
COPY source /package
RUN pip install --editable .
RUN bash -c 'mv *.egg-info $(python -c "import site; print(site.getsitepackages()[0])")'
RUN python setup.py clean


COPY credentials.json /
ENV GOOGLE_APPLICATION_CREDENTIALS /credentials.json

CMD ["pubsub_emulator"]

EXPOSE 8042
