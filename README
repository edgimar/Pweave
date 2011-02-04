.. -*- restructuredtext -*-

.. _README:

About Pweave
============

Pweave is a text preprocessor, for textfiles containing special blocks of code.
These blocks are processed and replaced with the processing results.  At the
beginning of each block, one can specify a *processor* to use for processing
the block, as well as specifying one or more options to provide to the
processor.  In the case that no processor or options are specified, a default
processor will be used with default options (see `Processors`_ below for more
details on the available processors).


Installation
============

Pweave is just a single python script which you can place anywhere you wish.
In addition, there are several text-processing plugins which enable more
powerful and specific processing of code-blocks (a.k.a. chunks) in a pweave
source file.  To make a plugin available when running pweave, simply place its
.py file in one of the following three directories:

  * [any directory specified using the -p argument when running pweave]
  * <directory containing source-file>/pweave_plugins
  * ~/.pweave_plugins

The plugins included with pweave can be found in the pweave_plugins directory,
which is in the same directory as this README file.  Additionally, any
non-plugin python file or module that you wish to import from within a
code-block can be placed in one of the three directories above, because these
directories are added to sys.path.


Quick Start
===========

As a quick demonstration of how to use pweave, do the follwing:

1. Create a pweave source file called `test.rst_pweave` which contains::

     This is a test.

     <<p=default, echo=false>>=
     print "Hello " + "World"
     print range(10)
     @
     
     Here's some text after the test.

2. Run pweave on this file::

     python pweave.py test.rst_pweave

That's it!  Pweave should have generated two files for you, a preprocessed
document file (by default a reStructuredText file) and a python file.  The document
file will contain the contents of `test.rst_pweave`, where the code block has been
replaced by the results of evaluating the code within the code block.  The
python file will contain the contents of the code block (or multiple code
blocks if there were more than one).


Code Blocks
===========

A code block (also known as a *chunk* in the world of literate programming) has the following form::

    <<BLOCK-OPTIONS>>=
    BLOCK-CONTENTS
    @

BLOCK-OPTIONS contains an optional block-name string, (optionally) followed by
one or more options.  A couple examples to clarify:

* **<<myname>>=**   -- only specifies a block-name
* **<<myname, opt1=a, opt2=b>>=**  -- specifies a name and two options
* **<<p=default, opt1="well, yes">>=** -- specifies that the 'default' processor should be used.
  Option values containing commas should be surrounded by *double* quotation marks.

BLOCK-CONTENTS can contain any number of lines (including none).  Code blocks cannot be
nested within one another.


Processors
==========

A processor is responsible for handling the contents of a block, performing
certain operations, and returning text to replace the block with in the
preprocessed document (i.e. the output of pweave). Depending on the kind of
processor that handles a block, a block could contain anything from ordinary
text to source-code (which could potentially be executed/evaluated by the
processor).  

Below is a catalog of processors bundled with pweave.  The 'default' processor
is included directly in pweave, whereas all other processors are available as
"processor plugins", and can be found in the pweave_plugins folder.


Default
-------

The default processor has various options for how to include/process python
code-blocks.  For more information, refer to the "code chunk options" section
of the sphinx-generated documentation (run make from within the doc folder), or
in the associated sourcefile *doc/usage.rst*.


Matplotlib Figure Plugin (mplfig)
---------------------------------

Given a code-block containing sourcecode required to generate a matplotlib
figure, a PDF file of this figure will be stored, and the LaTeX snippet
required for including the image in a LaTeX figure will be generated. 
            

Table Plugin (table)
--------------------

Execute a code-block, and generate a LaTeX table from a set of python lists
which specify table elements (i.e. what to populate the table's rows and
labels with).


AutoWrap Plugin (autowrap)
--------------------------

Wraps specified substrings in the code-block with an arbitrary LaTeX command,
and inserts the code-block into the output document with these substrings
replaced with their wrapped equivalents.  One example of how this can be used
is when one wants to select certain mathematical symbols in an equation to
automatically make bold.


\[Add Your Own Plugin Here\]
----------------------------

If you have a fantastic idea for a processor plugin, and wish to contribute it,
please do!

