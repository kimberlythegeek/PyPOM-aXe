pypom-axe
##########

pypom-axe integrates the aXe accessibility testing API with PyPOM.


.. image:: https://img.shields.io/badge/license-MPL%202.0-blue.svg?style=plastic
   :target: https://github.com/kimberlythegeek/pypom-axe/blob/master/LICENSE.txt
   :alt: License
.. image:: https://img.shields.io/pypi/v/pypom-axe.svg?style=plastic
   :target: https://pypi.org/project/pypom-axe/
   :alt: PyPI
.. image:: https://img.shields.io/pypi/wheel/pypom-axe.svg?style=plastic
   :target: https://pypi.org/project/pypom-axe/
   :alt: wheel
.. image:: https://img.shields.io/github/issues-raw/kimberlythegeek/pypom-axe.svg?style=plastic
   :target: https://github.com/kimberlythegeek/pypom-axe/issues
   :alt: Issues

Requirements
*************

You will need the following prerequisites in order to use pypom-axe:

- Python 2.7 or 3.6
- PyPOM >= 1.2.0

Installation
*************

To install pypom-axe:

.. code-block:: bash

  $ pip install pypom-axe

Usage
*************

``pypom-axe`` will run the aXe accessibility checks by default whenever its ``wait_for_page_to_load()`` method is called.

If you overload ``wait_for_page_to_load()``, you will need to call ``super([YOUR CLASS NAME], self).wait_for_page_to_load()`` within your overloaded method.

*base.py*

.. code-block:: python

   from pypom_axe import AxePage as Page

   class Base(Page):

   def wait_for_page_to_load(self, context=None, options=None, impact=None):
     super(Base, self).wait_for_page_to_load()
     self.wait.until(lambda s: self.seed_url in s.current_url)
     return self

You also have the option to customize the accessibility analysis using the
parameters ``context``, ``options``, and ``impact``. ``context`` and ``options``
directly reflect `the parameters used in axe-core <https://github.com/dequelabs/axe-core/blob/master/doc/API.md#api-name-axerun>`_.

``impact`` allows you to specify the impact level you wish to check for.

Running with an impact of ``minor`` checks for any violations with a severity of
``minor`` or higher.

The same applies to running with an impact of ``serious``.

An impact of ``critical`` will only check for critical violations.

.. code-block:: python

  from pypom_axe import AxePage as Page

  class Base(Page):

  def wait_for_page_to_load(self, context=None, options=None, impact=None):
    super(Base, self).wait_for_page_to_load(None, None, 'serious')
    self.wait.until(lambda s: self.seed_url in s.current_url)
    return self

Resources
===========

- `Issue Tracker <https://github.com/kimberlythegeek/pypom-axe/issues>`_
- `Code <https://github.com/kimberlythegeek/pypom-axe>`_
