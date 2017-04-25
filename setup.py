from setuptools import setup, find_packages

setup(
    name='ftport',
    version='0.0.1',
    description='Python ftplib extension for registering an alternative IP for'
                ' the PORT command',
    url='https://github.com/jgomo3/ftport',
    author='Jesús Gómez',
    author_email='jgomo3@gmail.com',
    license='MIT',
    packages=['ftport'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',  
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Internet :: File Transfer Protocol (FTP)',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    keywords='ftp-client ftp',
)
