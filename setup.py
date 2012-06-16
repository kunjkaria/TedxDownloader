from setuptools import setup, find_packages
setup(
    name='tedxDownloader',
    version='0.1.0',
    author='Kunj Karia',
    author_email='kunj.karia91@gmail.com',
    packages=find_packages(),
    description='Download Tedx Videos',
    package_data={"tedtalks":["html/ted.html"]},
    scripts=["tedtalks/scripts/teddownload"]
)
