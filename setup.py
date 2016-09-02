from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pgh-next-rgbus',
    version='0.0.1',
    description='Display arrival times for Pittsburgh Port Authority buses on an RGB matrix',
    author='John Berry',
    author_email='ulfmagnetics@gmail.com',
    url='https://github.com/ulfmagnetics/pgh-next-rgbus',
    license=license,
    packages=find_packages()
)

