from setuptools import setup

import io
import os


here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read('README.md')


setup(
    name='pymaxcul',
    version='0.1.13',
    url='https://github.com/maufl/pymaxcul',
    license='BSD License',
    author='Markus Ullmann, Karl Wolffgang, Felix Maurer',
    tests_require=['pytest>=3.0.5'],
    install_requires=['pyserial>=3.1.1'],
    author_email='github@maufl.de',
    description='Talk to eq-3 MAX! devices using a CUL stick',
    long_description=long_description,
    packages=['maxcul'],
    include_package_data=True,
    platforms='any',
    test_suite='maxcul.test.test_maxcul',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Home Automation'
    ],
    extras_require={
        'testing': ['pytest'],
    }
)
