# adapted from
# https://github.com/thet/your.app/blob/master/setup.py
from setuptools import setup, find_packages
#import sys, os


version = '0.1'
shortdesc = 'example cone.app app'
longdesc = ''

setup(name='my.app',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
      keywords='',
      author='Anne Gilles',
      author_email='anne@shri.de',
      url=u'https://github.com/AnneGilles/my.app',
      license='GNU General Public Licence',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['my'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'cone.app',
      ],
      )
