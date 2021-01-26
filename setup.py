from setuptools import setup

setup(name='pyconsul',
      version='0.1',
      description='Consul client for Python',
      url='https://github.com/shrivatsas/pyconsul',
      author='shrivatsas',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['pyconsul'],
      install_requires=[
          'httpx==0.16.1',
          'pydantic==1.7.3'
      ],
      zip_safe=False)
