from distutils.core import setup
setup(
    name='xssh',
    version='0.2',
    author='Syed Ali',
    author_email='syed_a_ali@yahoo.com',
    packages=['xssh'],
    scripts=['bin/xssh'],
    url='http://pypi.python.org/pypi/xssh/',
    license='LICENSE.txt',
    description='SSH Multiplexer.',
    long_description=open('README.txt').read(),
    install_requires=[
        "argparse >= 1.2.1",
        "crypto >= 1.1.0",
        "paramiko >= 1.11.0",
    ],
)
