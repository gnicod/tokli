from setuptools import setup

setup(name='tokli',
      version='0.1',
      description='tokli',
      url='http://github.com/gnicod/tokli',
      license='MIT',
      packages=['tokli'],
      install_requires=[
          'requests', 'requests_oauthlib', 'oauthlib'
      ],
      scripts=['bin/tokli'],
      zip_safe=False)
