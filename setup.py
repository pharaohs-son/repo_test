from setuptools import setup, find_packages

# setar as versoes sertinho (>=x ou ==x)
requirements = [
               'biopython==1.73',
               'pkgutil'
                ]

with open('README.md') as rm:
    long_description = rm.read()

setup(
    name="Test_Setup",
    version='1.0',
    packages=find_packages(include=["scripts"]),
    description='setup teste',
    long_description=long_description,
    install_requires=requirements,
    author='Vilmar Benetti Filho',
    author_email='labinfo.ufsc@gmail.com',
    scripts=['scripts/main_teste.py'],
    data_files=[('config', ['scripts/config.config'])],
    zip_safe=False,
    include_package_data=True,
    python_requires=">=3",
    url='https://github.com/pharaohs-son/repo_test.git',
    download_url='https://github.com/pharaohs-son/repo_test/archive/refs/heads/master.zip'
)
