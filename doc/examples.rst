reST example
-------------

Here is a simple example of a Pweave file (`ma.Pnw <_static/ma.Pnw>`_) that uses reST as the documentation format. The file has two code chunks of which second one also produces a figure that is included in the output.

.. literalinclude:: ma.Pnw

The file was processed with Pweave using:

:: 

  Pweave ma.Pnw

And as result we get the reST document `ma.rst <_static/ma.rst>`_ (shown below), which can be turned into pdf using rst2latex and pdflatex: `ma.pdf <_static/ma.pdf>`_. 

.. literalinclude:: ma.rst

Ouput of the example in Sphinx
------------------------------

The produced rst file can of course also be included in a Sphinx document, like this website using ".. include:: ma.rst". Here is what it looks like:

.. include:: ma.rst