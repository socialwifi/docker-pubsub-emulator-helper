from pip.req import parse_requirements
from setuptools import find_packages
from setuptools import setup


setup(
    name='sw-pubsub-emulator-helper',
    version='1.0',
    packages=find_packages(exclude=['tests']),
    install_requires=[str(ir.req) for ir in parse_requirements('base_requirements.txt', session=False)],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'pubsub_emulator = pubsub_emulator_helper:run',
            'pubsub_add_topic = pubsub_emulator_helper:add_topic',
            'pubsub_add_subscription = pubsub_emulator_helper:add_subscription',
        ],
    },
)
