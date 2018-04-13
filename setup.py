# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from setuptools import find_packages, setup


def readme():
    with open('./README.rst') as f:
        readme = f.read()
    with open('./CHANGELOG.rst') as f:
        log = f.read()
    return readme + '\n\n' + log


setup(name='PyPOM-aXe',
      version='1.0.0',
      description='PyPOM-aXe is a plugin for PyPOM to integrate \
                accessibility tests using the aXe API.',
      long_description=readme(),
      url='https://github.com/kimberlythegeek/pypom-axe',
      author='Kimberly Sereduck',
      author_email='ksereduck@mozilla.com',
      packages=['PyPOM_aXe'],
      package_data={'PyPOM_aXe': ['src/axe.min.js'], },
      install_requires=['PyPOM>=2.0.0rc'],
      entry_points={'pypom.plugin': ['axe = PyPOM_aXe.axe']},
      license='Mozilla Public License 2.0 (MPL 2.0)',
      keywords='axe-core pypom accessibility automation mozilla',
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6'])
