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


setup(name='pypom-axe',
      version='0.1.0',
      description='pypom-axe is a PyPOM extension to integrate \
                accessibility tests using the aXe API.',
      long_description=readme(),
      url='https://github.com/kimberlythegeek/pypom-axe',
      author='Kimberly Sereduck',
      author_email='ksereduck@mozilla.com',
      packages=find_packages(),
      package_data={'pypom_axe': ['src/axe.min.js'], },
      install_requires=[
          'pypom>=1.2.0'
      ],
      license='Mozilla Public License 2.0 (MPL 2.0)',
      keywords='axe-core pypom accessibility automation mozilla')
