from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='ufcpy',
    version='3.0.0',
    author='youngtrep',
    author_email='youngtrep.business@gmail.com',
    description='A fast and easy way to access the UFC roster',
    long_description=long_description,
    url='https://github.com/YoungTrep/ufcpy',
    packages=find_packages(),
    install_requires= [
        'beautifulsoup4 >= 4.12.3',
        'requests >= 2.32.3', 
        'lxml >= 5.3.0'
    ],
    license='MIT',
    keywords=['ufc', 'mma', 'mixed martial arts', 'fighting', 'fighters', 'ufc-api', 'mma-api'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3.8'
)
