from setuptools import setup, find_packages

setup(
    name='dynamic_settings',
    version='0.0.1',
    url='',
    license='',
    author='Georgij',
    author_email='',
    description='',
    zip_safe=False,
    packages=find_packages(
        where='src',
        # include=['my_package', 'my_package.*'],
        # exclude=['my_package_test', 'my_package_test.*']
    ),
    package_dir={'': 'src'},
)
