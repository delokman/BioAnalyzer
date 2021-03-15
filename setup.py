from setuptools import setup, find_packages
 
# See note below for more information about classifiers
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: ',
    'Operating System :: POSIX :: Linux :: Windows',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3'
]
 
setup(
  name='bioanalyzer',
  version='0.0.1',
  description='BioAnalyzer is a module that allows you to extract personnals informations from an instagram profile bio such as : Religion, Hobbies, Ethnicity, Emails, Paypal.me/, Snapchat, Twitter, Best Friends, Age, Location, Love Relationship, Love Relationship date, Facebooks, Astrologic Sign, Sexuality.',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/dalunacrobate/BioAnalyzer',
  author='Dalunacrobate',
  author_email='daluna_pro@protonmail.ch',
  classifiers=classifiers,
  entry_points = {'console_scripts': ['bioanalyzer = BioAnalyzer:main']},
  keywords='osint instagram bio intelligence recon reconnaissance api social-media',
  packages=find_packages(),
  install_requires=['requests','bs4','colorama']
)