from setuptools import setup, find_packages


setup(
    name='canopy',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Click',
        'SQLAlchemy',
        'python-dotenv',
        'psycopg2-binary'
    ],
    entry_points={
        'console_scripts': [
            'canopy = app.commands_registrator:cli',
        ],
    },
)
