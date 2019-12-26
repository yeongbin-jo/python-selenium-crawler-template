# coding: utf-8
import os
import sys

from setuptools import setup


__author__ = 'Yeongbin Jo <yeongbin.jo@pylab.co>'
__license__ = "GPLv3"

__version__ = "0.1.0"
__maintainer__ = "Yeongbin Jo"
__email__ = "yeongbin.jo@pylab.co"
__status__ = "Production"


with open('README.md') as readme_file:
    long_description = readme_file.read()


# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()
elif sys.argv[-1] == 'clean':
    import shutil
    if os.path.isdir('build'):
        shutil.rmtree('build')
    if os.path.isdir('dist'):
        shutil.rmtree('dist')
    if os.path.isdir('selenium_crawler_template.egg-info'):
        shutil.rmtree('selenium_crawler_template.egg-info')


setup(
    name="selenium-crawler-template",
    version="0.1.0",
    author="Yeongbin Jo",
    author_email="yeongbin.jo@pylab.co",
    description="Boilerplate for developing crawler with Selenium.",
    license="MIT",
    keywords="chromedriver chrome selenium splinter",
    url="https://github.com/yeongbin-jo/python-selenium-crawler-template",
    packages=['selenium_crawler_template'],
    long_description_content_type='text/markdown',
    long_description=long_description,
    python_requires='>=3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Installation/Setup',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
