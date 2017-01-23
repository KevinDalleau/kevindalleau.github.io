from setuptools import setup

setup(name='graph2vec',
      version='0.1',
      description='A package with module to vectorize graphs',
      url='http://github.com/KevinDalleau/graphVectorizer',
      author='Kevin Dalleau',
      author_email='',
      license='GNU GENERAL PUBLIC LICENSE',
      py_modules=['vectorizer'],
      install_requires=['numpy','rdflib'])
