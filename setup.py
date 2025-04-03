#!/usr/bin/env python

from setuptools import setup

setup(name='tap-google-ads',
      version='1.8.0',
      description='Singer.io tap for extracting data from the Google Ads API',
      author='Stitch',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_google_ads'],
      install_requires=[
          'singer-python==6.0.0',
          'requests==2.26.0',
          'backoff==2.2.1',
          'google-ads==21.1.0',
      

          # Necessary to handle gRPC exceptions properly, documented
          # in an issue here: https://github.com/googleapis/python-api-core/issues/301
            'protobuf==4.25.3',  # Highest 4.x version (proven stable)
          'grpcio-status==1.48.2',  # Downgraded to match protobuf 4.x
      ],
      extras_require= {
          'dev': [
              'pylint',
              'nose',
              'ipdb',
          ]
      },
      entry_points='''
          [console_scripts]
          tap-google-ads=tap_google_ads:main
      ''',
      packages=['tap_google_ads'],
      package_data = {
      },
      include_package_data=True,
)
