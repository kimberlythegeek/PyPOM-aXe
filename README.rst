pypom-axe
==========

``pypom-axe`` integrates the aXe accessibility testing API with PyPOM.

Requirements
-------------

You will need the following prerequisites in order to use pypom-axe:

- Python 2.7 or 3.6
- PyPOM >= 1.2.0

Installation
-------------

To install pypom-axe:

.. code-block:: bash

  $ pip install pypom-axe -i https://testpypi.python.org

Usage
------

``pypom-axe`` will run the aXe accessibility checks by default whenever its ``wait_for_page_to_load()`` method is called.

If you overload ``wait_for_page_to_load()``, you will need to call ``super([YOUR CLASS NAME], self).wait_for_page_to_load()`` within your overloaded method.

*base.py*

.. code-block:: python

   from pypom_axe import AxePage as Page

   class Base(Page):

   def wait_for_page_to_load(self):
     super(Base, self).wait_for_page_to_load()
     self.wait.until(lambda s: self.seed_url in s.current_url)
     return self


Resources
----------

- `Issue Tracker <https://github.com/kimberlythegeek/pypom-axe/issues>`_
- `Code <https://github.com/kimberlythegeek/pypom-axe>`_
