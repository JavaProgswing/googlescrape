from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

README = open('CHANGELOG.txt').read()+"\n\n"
with open("README.md", "r") as f:
  README = README+f.read()

setup(
  name='googlescrape',
  version='0.0.4',
  description='This is a python api to scrape search results from a url.',
  long_description=README,
  long_description_content_type="text/markdown",
  url='https://github.com/JavaProgswing/googlescrape',
  author='JavaProgswing',
  author_email='thejavaprofessional@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='googlescrape',
  packages=find_packages(),
  install_requires=['selenium >= 4.1.0','beautifulsoup4 >= 4.10.0','webdriver-manager == 3.5.2','validators >= 0.18.2']
)