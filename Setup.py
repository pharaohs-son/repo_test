from setuptools import setup, find_packages

# setar as versoes sertinho (>=x ou ==x)
requirements = [
                'Bio>=1.73',
                ]

with open('README.md') as rm:
    long_description = rm.read()

setup(
    name="Test_Setup",
    packages=find_packages(),
    version='1.0',
    description='setup.py teste',
    long_description=long_description,
    install_requires=requirements,
    author='Vilmar Benetti Filho',
    author_email='labinfo.ufsc@gmail.com',
    zip_safe=False,
    include_package_data=True,
    python_requires=">=3",
    url='https://github.com/pharaohs-son/repo_test.git',
    download_url='https://github.com/pharaohs-son/repo_test/archive/refs/heads/master.zip',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',  # pathlib is born
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
