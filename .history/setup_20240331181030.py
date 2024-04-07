from setuptools import setup

setup(
    name='Lash-Designer',
    version='1.0',
    packages=['Lash'],
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
    ],
)
