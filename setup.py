from setuptools import setup


setup(
    name='vagabond',
    version='1.0',
    url='http://github.com/cburmeister/vagabond/',
    license='MIT',
    author='Corey Burmeister',
    author_email='burmeister.corey@gmail.com',
    description='Search https://www.airbnb.com/ without leaving the prompt.',
    py_modules=['vagabond'],
    platforms='any',
    install_requires=[
        'beautifulsoup4==4.3.2',
        'click==3.3',
        'requests==2.5.1',
        'Werkzeug==0.10.1',
    ],
    entry_points='''
        [console_scripts]
        vagabond=vagabond:main
    '''
)
