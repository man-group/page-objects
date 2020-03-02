from distutils.core import setup

setup(
    name='page-objects',
    version='1.1.0',
    packages=['page_objects'],
    url='https://github.com/krizo/page-objects.git',
    license='MIT',
    author='Edward Easton',
    author_email='eeaston@gmail.com',
    description='Page Objects for Python', requires=['selenium', 'pytest', 'mock']
)
