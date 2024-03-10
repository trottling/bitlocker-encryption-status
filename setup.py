from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='bitlocker_encryption_status',
    version='0.0.1',
    author='trottling',
    author_email='kernel6@duck.com',
    description='Library for get BitLocker-encrypted drives status using Python .',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/trottling/bitlocker-encryption-status',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
    ],
    keywords='bitlocker encryption status',
    project_urls={
        'GitHub': 'https://github.com/trottling/bitlocker-encryption-status'
    },
    python_requires='>=3.6'
)
