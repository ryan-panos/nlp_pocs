
from setuptools import setup, find_packages

setup(
    name="flaskular",
    version="0.1",
    packages=find_packages(),
    scripts = ['scripts/runserver.py', 'scripts/manage.py'],
    package_data = { 
        'flaskular': ['static', 'templates'], 
    },
    zip_safe=False,
    install_requires=['Flask'],
)
