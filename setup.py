from setuptools import setup, find_packages

setup(
    name='amazon-shopping-agent',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    test_suite='tests',
) 