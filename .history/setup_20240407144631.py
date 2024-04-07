from setuptools import setup

setup(
    packages=['Lash-Designer'],
    version='1.0',
    packages=['Lash-Designer'],
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-Cors',
        'Sqlite3',
        'Pytest',
        'Python-Dotenv'
    ],
)
