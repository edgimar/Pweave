.. Pweave - literate programming with Python documentation master file, created by
   sphinx-quickstart on Thu Mar  4 14:50:07 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction
------------
Welcome to Pweave website and documentation. Pweave is a literate programming tool for Python that is developed after `Sweave <http://www.stat.uni-muenchen.de/~leisch/Sweave/>`_. Pweave is a single python script that is able to weave a python code between “<<>>=” and “@” blocks and include the results in the document. Pweave is good for creating dynamic reports and tutorials. 

**Features**

* Execute python code in the blocks and capture input and ouput to a literate environment using  either `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ or Latex source. Using reST enables conversion of the documents to several formats (html, latex, pdf, odt).
* Use hidden code blocks, i.e. code is executed, but not printed in the output file.
* Capture matplotlib graphics.


Download
_________
Download the latest stable here: `Pweave <http://files.mpastell.com/Pweave>`_. You can also checkout the latest code with mercurial using:

::
 
 hg clone https://pweave.googlecode.com/hg/ pweave 

Install
_____________
To install **Pweave** simply copy the "Pweave" file to a directory in your path and make it executable e.g. using:

::

 cp Pweave /usr/local/bin
 chmod a+xr /usr/local/bin/Pweave

Help
______________

.. toctree::
   :maxdepth: 2

   usage.rst
   examples.rst




