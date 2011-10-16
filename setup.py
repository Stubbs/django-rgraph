#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-rgraph',
    version='0.1',
    description='RGraph tamplate tags for Django',

    author='Stuart Grimshaw',
    author_email='stuart.grimshaw@gmail.com',
    license='Simplified BSD',
    url='',

    packages=find_packages(exclude=['tests.*', 'tests', 'example.*', 'example']),
    include_package_data=True,  # declarations in MANIFEST.in

    install_requires=['Django >=1.1'],
    tests_require=['Django >=1.1', 'Attest >=0.4', 'django-attest', 'fudge'],

    test_loader='attest:FancyReporter.test_loader',
    test_suite='tests.everything',

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
)
