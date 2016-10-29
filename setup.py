from setuptools import setup, find_packages
from io import open

setup(
    name='django-flowjs',
    version='0.1',
    description='This is an app for Django projects to enable large uploads using flow.js',
    long_description=open('README.md', encoding='utf-8').read(),
    author='Jai Vikram Singh Verma',
    author_email='jaivikram.verma@gmail.com',
    url='https://github.com/jaivikram/django-flowjs',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django>=1.4',
    ],
    classifiers=[
        'Development Status :: 1 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
