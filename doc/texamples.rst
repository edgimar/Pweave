
.. index:: LaTeX example

LaTeX example
-------------

`Here <_static/ma-tex.pdf>`_ is a simple example of a Pweave file (`ma-tex.Plw <_static/ma-tex.Plw>`_) that uses LaTeX as the documentation markup. The file demonstrates basic usage of Pweave and how it can easily be used to add dynamic figures and tables. 

.. literalinclude:: ma-tex.Plw

The file was processed with Pweave using:

:: 

  Pweave -f tex ma.Plw

And as result we get the LaTex document `ma-tex.tex <_static/ma-tex.tex>`_ (shown below).  

.. literalinclude:: ma-tex.tex


Processing the example with pdflatex produces `this pdf <_static/ma-tex.pdf>`_
