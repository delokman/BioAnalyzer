from setuptools import setup, find_packages

setup(
    name='bioanalyzer',
    version="0.0.1",
    packages=find_packages(),
    author="Dalunacrobate",
    author_email="daluna_pro@protonmail.ch",
    install_requires=["requests","bs4","colorama","argparse"],
    description="BioAnalyzer is a module that allows you to extract personnals informations from an instagram profile bio such as : Religion, Hobbies, Ethnicity, Emails, Paypal.me/, Snapchat, Twitter, Best Friends, Age, Location, Love Relationship, Love Relationship date, Facebooks, Astrologic Sign, Sexuality.",
    include_package_data=True,
    url='http://github.com/dalunacrobate/BioAnalyzer',
    entry_points = {'console_scripts': ['BioAnalyzer = BioAnalyzer.bioanalyzer:main']},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
