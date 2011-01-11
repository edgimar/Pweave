"""
This module defines a TableProcessor class for use with Pweave.

"""
# this plugin module is only imported by Pweave.py
import __main__ as pweave
CodeProcessor = pweave.CodeProcessor
options = pweave.options
plt = pweave.plt

import StringIO

class TableProcessor(CodeProcessor):
    """Processor for generating (LaTeX) tables.
    
    This processor generates a table from a nested-list.
    
    The following code-block options are accepted:
    
    *table_list_name* -- (optional) specifies the name of a nested list which
                         the code-block will create that contains the contents
                         of the table.  Each sublist in the list represents one
                         row of the table, and can contain either string or
                         numeric values.  By default, this option is set to
                         "table_rows". 
    
    *column_labels* -- (optional) specifies the name of a list which contains
                       the column labels. 
    
    *row_labels* -- (optional) specifies the name of a list which contains the
                    row labels.
    
    TODO: other formatting options
    
    """
    def name(self):
        return "table"
    
    # TODO: implement...

