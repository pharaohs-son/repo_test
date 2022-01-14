from setuptools import setup, find_packages

# setar as versoes sertinho (>=x ou ==x)
requirements = [
               'biopython==1.73',
                ]

with open('README.md') as rm:
    long_description = rm.read()

setup(
    name="Test_Setup",
    packages=find_packages(include=["scripts"]),
    scripts=['scripts/main_teste.py'],
    version='1.0',
    description='setup teste',
    long_description=long_description,
    install_requires=requirements,
    author='Vilmar Benetti Filho',
    author_email='labinfo.ufsc@gmail.com',
    zip_safe=False,
    package_data={'': ['*.config']},
    include_package_data=True,
    python_requires=">=3",
    url='https://github.com/pharaohs-son/repo_test.git',
    download_url='https://github.com/pharaohs-son/repo_test/archive/refs/heads/master.zip'
)
