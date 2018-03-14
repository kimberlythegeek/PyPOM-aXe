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
- PyPOM development version from my git fork

Installation
*************

To install PyPOM:

.. code-block:: bash

  $ pip install git+git://github.com/kimberlythegeek/pypom.git@pypom_hooks

To install pypom-axe:

.. code-block:: bash

  $ pip install git+git://github.com/kimberlythegeek/pypom-axe.git@pypom_hooks

Usage
*************

> This version of pypom-axe uses an experimental version of [PyPOM](https://github.com/kimberlythegeek/PyPOM/tree/pypom_hooks),
> where the basic usage has been modified. In order to use this version, both
> packages need to be installed from their respective git branches.

``pypom-axe`` will run the aXe accessibility checks by default whenever a page's
``open()`` method is called.

This version utilizes an experimental feature in PyPOM.

When using this version of PyPOM, you will overload ``_page_loaded``
instead of ``wait_for_page_to_load``.

Calling ``wait_for_page_to_load`` now calls the template methods
``_before_page_loads``,``_page_loaded``, and ``_after_page_loads``.

``pypom-axe`` runs accessibility tests ``_after_page_loads``.

*base.py*

.. code-block:: python

   from pypom_axe.axe import AxePage as Page

   class Base(Page):

   def _page_loaded(self, context=None, options=None, impact=None):
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
