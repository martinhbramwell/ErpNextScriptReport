from setuptools import setup, find_packages

setup(
    name='helloworld',
    version='0.0.1',
    description='A simple "Hello World" app for ERPNext',
    author='Your Name',
    author_email='you@example.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=('frappe',),
)
