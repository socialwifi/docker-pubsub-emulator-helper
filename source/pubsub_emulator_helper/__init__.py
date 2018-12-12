import os

import sys
from google.cloud import pubsub


def run():
    os.execvp(
        '/root/google-cloud-sdk/bin/gcloud', ['gcloud', 'beta', 'emulators', 'pubsub', 'start', '--host-port', '0.0.0.0:8042']
    )


def add_topic():
    ensure_emulator_usage()
    client = pubsub.Client()
    client.topic(sys.argv[1]).create()


def add_subscription():
    ensure_emulator_usage()
    client = pubsub.Client()
    topic = client.topic(sys.argv[1])
    topic.subscription(sys.argv[2]).create()


def ensure_emulator_usage():
    if 'PUBSUB_EMULATOR_HOST' not in os.environ:
        os.environ['PUBSUB_EMULATOR_HOST'] = 'localhost:8042'
