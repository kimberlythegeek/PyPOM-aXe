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

``pypom-axe`` will run the aXe accessibility checks by default whenever its
``wait_for_page_to_load()`` method is called.

If you overload ``wait_for_page_to_load()``, you will need to call
``super([YOUR CLASS NAME], self).wait_for_page_to_load()`` within your
overloaded method.

You can disable accessibility tests by setting the environment variable
``ACCESSIBILITY_DISABLED`` to ``true``.

You can **enable** output of the JSON results by setting the environment variable
``ACCESSIBILITY_REPORTING`` to ``true``. This will output files to ./results/,
which must be created if it does not already exist.

*base.py*

.. code-block:: python

   from pypom_axe.axe import AxePage as Page

   class Base(Page):

   def wait_for_page_to_load(self, context=None, options=None, impact=None):
     super(Base, self).wait_for_page_to_load()
     self.wait.until(lambda s: self.seed_url in s.current_url)
     return self

You also have the option to customize the accessibility analysis using the
parameters ``context``, ``options``, and ``impact``.

``context`` and ``options`` directly reflect the parameters used in axe-core.
For more information on ``context`` and ``options``, view the `aXe
documentation here <https://github.com/dequelabs/axe-core/blob/master/doc/API.md#parameters-axerun>`_.

The third parameter, ``impact``, allows you to filter violations by their impact
level.

The options are ``'critical'``, ``'serious'`` and ``'minor'``, with the
default value set to ``None``.

This will filter violations for the impact level specified, and **all violations with a higher impact level**.

.. code-block:: python

  from pypom_axe.axe import AxePage as Page

  class Base(Page):

  def wait_for_page_to_load(self, context=None, options=None, impact=None):
    super(Base, self).wait_for_page_to_load(None, None, 'serious')
    self.wait.until(lambda s: self.seed_url in s.current_url)
    return self

Resources
===========

- `Issue Tracker <https://github.com/kimberlythegeek/pypom-axe/issues>`_
- `Code <https://github.com/kimberlythegeek/pypom-axe>`_
