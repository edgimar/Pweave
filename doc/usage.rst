
.. raw:: latex

 \pagebreak

Pweave Help
===============

Features
______________________

`Pweave <http://mpastell.com/pweave>`_ is a literate programming tool for Python that is developed
after `Sweave <http://www.stat.uni-muenchen.de/~leisch/Sweave/>`_. And
like Sweave it uses the `noweb <http://www.cs.tufts.edu/~nr/noweb/>`_
syntax. Pweave is a single python script that is able to weave a
python code between “<<>>=” and “@” blocks and include the results in
the document. Pweave is good for creating dynamic reports and
tutorials. 

**Features**

* Execute python code in the blocks and capture input and ouput to a literate environment using  either `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ or Latex source. Using reST enables conversion of the documents to several formats (html, latex, pdf, odt).
* Use hidden code blocks, i.e. code is executed, but not printed in the output file.
* Capture matplotlib graphics.

Document types
________________

* **Source document:** Contains a mixture of documentation and code chunks. Pweave will evaluate the code and leave the documentation chunks as they are. The documentation chunks can be written either with reST or Latex. The source document is processed using *Pweave*, which gives us the formatted output document.

* **Output document:** Contains the documentation, original code, the captured outputof the code and optionally captured `matplotlib <http://matplotlib.sourceforge.net/>`_ figures   

Pweave syntax
_____________
Pweave uses noweb syntax for defining the code chunks and documentation chunks, just like `Sweave <http://www.stat.uni-muenchen.de/~leisch/Sweave/>`_. 

* **Code chunks** start with a line marked with <<>>= or <<option>>= and end with line marked with @. The code between the start and end markers is executed and the output is captured to the output document.

* **Documentation chunks** Are the rest of the document (between @ and <<>>= lines) and can be written using either reST or Latex.

Options
_______
Pweave currently has the following options for processing the code chunks (e.g. <<fig=True>>=):

* **fig:** True or (False). Whether a matplotlib plot produced by the code chunk should be included in the file.
* **echo:** True or (False). Echo the python code in the output document.
* **eval:** True or (False). Evaluate the code chunk,
* **results:** "verbatim", (“rst”, “tex”). The output format of the printed results.

Calling Pweave
_______________

Processing a reST source document:

::

  Pweave source.Pnw

Processing a Latex document:

:: 

  Pweave -f tex source.Pnw

Get options:

::

  Pweave --help

