Documentation for the Code
**************************

.. automodule:: aneris


useful #1 -- auto members
=========================

This is something I want to say that is not in the docstring.

.. automodule:: aneris.example.useful_1
   :members:

useful #2 -- explicit members
=============================

This is something I want to say that is not in the docstring.

.. automodule:: aneris.example.useful_2
   :members: public_fn_with_sphinxy_docstring, _private_fn_with_docstring

.. autoclass:: aneris.example.useful_2.MyPublicClass
   :members: get_foobar, _get_baz
