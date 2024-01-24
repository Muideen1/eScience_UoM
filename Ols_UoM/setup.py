from setuptools import setup, find_packages

setup(
    name='ols-cli',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ols=ols.ols:fetch_ontology_info_cli',
        ],
    },
    install_requires=[
        'requests',
    ],
    author='Muideen Ajagbe',
    author_email='muid.deen1@gmail.com',
    description='A command line tool to fetch ontology information using the OLS API.',
    keywords='OLS Ontology API',
)
