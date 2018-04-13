CHANGELOG
===========

version 1.0.0
^^^^^^^^^^^^^^
- Updated aXe to 3.0.1
- Updated PyPOM requirement to version 2.0.0
- Modified PyPOM-aXe to be used as a plugin for PyPOM, instead of inheriting it.

version 0.1.0
^^^^^^^^^^^^^^
- Enabled the use of two new environment variables.

1. ``ACCESSIBILITY_DISABLED=true`` will disable accessibility tests.
2. ``ACCESSIBILITY_REPORTING=false`` will **enable** the output of JSON results.

version 0.0.7
^^^^^^^^^^^^^^
- Modified impact_included class method to reflect changes to the aXe API:
- There are now only 3 impact levels: ``'critical'``, ``'serious'``, and ``'minor'``
