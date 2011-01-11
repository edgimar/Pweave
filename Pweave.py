#!/usr/bin/python

# Pweave, Literate programming tool for Python 
# ============================================
# 
# :Author: Matti Pastell <matti.pastell@helsinki.fi>
# :Website: http://mpastell.com
# Version: 0.12

import sys
import StringIO
import re
from optparse import OptionParser
import os
exec_namespace = {} # global (and local) namespace for exec()'ed code

class CodeProcessor(object):
    "Base Class for code-processor classes, used for processing code blocks"
    def __init__(self, execution_namespace=None):
        """
        *codeblock_options* -- a dictionary containing options specified for
                               the code-block.
        *execution_namespace* -- a namespace dictionary used for executing
                                 the code.
        """
        if execution_namespace is None:
            # by default, use the namespace defined globally in this module
            execution_namespace = exec_namespace
        
        self.execution_namespace = execution_namespace
        self.default_options = {}
    
    def name(self):
        "Return a string representing the name of this code-processor"
        raise NotImplementedError
    
    def set_default_options(self, codeblock_options):
        self.default_options = codeblock_options
    
    def process_code(self, codeblock, codeblock_options=None):
        """Process a code-block; return text to include in output documents.
        
        This method must do something with the (possibly multi-line) string
        *codeblock*, and return two strings -- one to be included in the
        'output' file (e.g. a LaTeX file), and one to be included in the
        generated python file.
        
        """
        raise NotImplementedError
        
        if codeblock_options is None:
            codeblock_options = self.default_options
        
        # ... build document_text and code_text strings, etc.  ...
        
        return (document_text, code_text)

    def exec_code(self, code_as_string):
        """Execute a block of code it's own (persistent) global namespace.
        
        *code_as_string* is executed as a chunk of python code within a
        namespace separate from that of this module.  The output produced
        by this code is returned.
        
        """
        tmp = StringIO.StringIO()
        sys.stdout = tmp
        
        # execute code, capturing stdout to tmp
        try:
            print(eval(code_as_string))
        except:
            exec(code_as_string, exec_namespace)
        result = tmp.getvalue()
        
        # stop capturing and restore normal stdout
        sys.stdout = sys.__stdout__
        tmp.close()
        
        return result

class DefaultProcessor(CodeProcessor):
    def __init__(self):
        super(DefaultProcessor, self).__init__()
        self.nfig = 1
    
    def name(self):
        "Return a string representing the name of this code-processor"
        return 'default'

    def process_code(self, codeblock, codeblock_options=None):
        outbuf = StringIO.StringIO() # temporary file obj for storing text
        if codeblock_options is None:
            codeblock_options = self.default_options
        blockoptions = codeblock_options
        
        # Format specific options for tex or rst
        if options.format == 'tex':
            codestart = '\\begin{verbatim}\n' 
            codeend = '\\end{verbatim}\n'
            outputstart = '\\begin{verbatim}\n'
            outputend = '\\end{verbatim}\n' 
            codeindent = ''
        elif options.format == 'rst':
            codestart = '::\n\n' 
            codeend = '\n\n'
            outputstart = '::\n\n' 
            outputend = '\n\n' 
            codeindent = '  '
        elif options.format == 'sphinx':
            codestart = '::\n\n' 
            codeend = '\n\n'
            outputstart = '::\n\n' 
            outputend = '\n\n' 
            codeindent = '  '
        
        #Output in doctests mode
        #print dtmode
        if blockoptions['term']:
            outbuf.write('\n')
            if options.format=="tex": outbuf.write(codestart)  
            
            for x in codeblock.splitlines():
                outbuf.write('>>> ' + x + '\n')
                result = self.exec_code(x)
                if len(result) > 0:
                    outbuf.write(result)
            
            result = ''
            outbuf.write(codeend)
        else:
            #include source in output file?
            if blockoptions['echo']==True:
                outbuf.write(codestart)
                for x in codeblock.splitlines():
                    outbuf.write(codeindent + x + '\n')
                outbuf.write(codeend)

            #evaluate code and include results in output file?
            if blockoptions['evaluate']==True:
                if blockoptions['fig']:
                    #A placeholder for figure options
                    #import matplotlib
                    #matplotlib.rcParams['figure.figsize'] = (6, 4.5)
                    pass
                
                result = self.exec_code(codeblock).splitlines()
        
        #If we get results they are printed
        if len(result) > 0:
            #TODO: fix -- if results != "verbatim" and !=rst and !=tex, 
            #      then indent isn't defined and code will break.
            if blockoptions['results'] == "verbatim":
                outbuf.write(outputstart)
                indent = codeindent
            
            if blockoptions['results'] == "rst" or blockoptions['results'] == "tex":
                indent = ''
            
            for x in result:
                outbuf.write(indent + x)
            outbuf.write('\n')
            
            if blockoptions['results'] == "verbatim":
                outbuf.write(outputend)
            result = ''
        
        #Save and include a figure?
        if blockoptions['fig']:
            figname = options.figdir + 'Fig' +str(self.nfig) + options.figfmt
            plt.savefig(figname, dpi = 200)
            
            if options.format == 'sphinx':
                figname2 = options.figdir + 'Fig' +str(self.nfig) +  options.sphinxtexfigfmt
                plt.savefig(figname2)
            plt.clf()
            if options.format == 'rst':
                if blockoptions['caption'] > 0:
                    #If the image has a caption, use Figure directive
                    outbuf.write('.. figure:: ' + figname + '\n')
                    outbuf.write('   :width: ' + width + '\n\n')
                    outbuf.write('   ' + blockoptions['caption'] + '\n\n')
                else:
                    outbuf.write('.. image:: ' + figname + '\n')
                    outbuf.write('   :width: ' + width + '\n\n')
            if options.format == 'sphinx':
                if blockoptions['caption'] > 0:
                    outbuf.write('.. figure:: ' + options.figdir + 'Fig' + str(self.nfig)  + '.*\n')
                    outbuf.write('   :width: ' + width + '\n\n')
                    outbuf.write('   ' + blockoptions['caption'] + '\n\n')
                else:
                    outbuf.write('.. image:: ' + options.figdir + 'Fig' + str(self.nfig)  + '.*\n')
                    outbuf.write('   :width: ' + width + '\n\n')
            if options.format == 'tex':
                if blockoptions['caption'] > 0:
                    outbuf.write('\\begin{figure}\n')
                    outbuf.write('\\includegraphics{'+ figname + '}\n')
                    outbuf.write('\\caption{' + blockoptions['caption'] + '}\n')
                    outbuf.write('\\end{figure}\n')
                else:
                    outbuf.write('\\includegraphics{'+ figname + '}\n\n')

            self.nfig += 1
        
        document_text = outbuf.getvalue()
        outbuf.close()
        
        return (document_text, codeblock) # document_text, code_text

# A function for parsing options
# TODO: parse in form <<processor_name, arg1=val1, arg2=val2, ...>>= where
#       processor_name is optional and defaults to 'default'
def get_options(optionstring):
    echo = True
    results = 'verbatim'
    fig = False
    evaluate = True
    width = '15 cm'
    caption = False
    term = False
    optionstring = re.sub(',', ';', optionstring)
    exec(optionstring)
    block_options = locals()
    return block_options


def run_pweave():
    codeprocessor = DefaultProcessor()
    
    # Is matplotlib used?
    if options.mplotlib.lower() == 'true':
        import matplotlib
        matplotlib.use('Agg')
        global plt
        import matplotlib.pyplot as plt
    
    # Format specific options for tex or rst
    if options.format == 'tex':
        figfmt = '.pdf'
        ext = 'tex'
    elif options.format == 'rst':
        figfmt = '.png'
        ext = 'rst'
    elif options.format == 'sphinx':
        figfmt = '.png'
        options.sphinxtexfigfmt = '.pdf'
        ext = 'rst'
    
    # Override the default fig format with command line option
    if options.figfmt > 0:
        options.figfmt = '.' + options.figfmt
    else:
        options.figfmt = figfmt
    
    # Open the file to be processed and get the output file name
    basename = infile.split('.')[0]
    outfile_fname = basename + '.' + ext
    pyfile_fname = basename + '.' + 'py'
    
    codefile = open(infile, 'r')
    outfile = open(outfile_fname, 'w')
    pyfile = open(pyfile_fname, 'w')
    
    lines = codefile.readlines()
    
    # Initialize some variables
    state = 'text'
    block = ''
    
    # Create figure directory if it doesn't exist
    if os.path.isdir(options.figdir) == False:
        os.mkdir(options.figdir)
    
    

    
    # Process the whole text file with a loop
    for line in lines:
        code = re.search('^<<(.*)>>=$', line.strip())
        
        # if at the start of a code block
        if code is not None:
            state = 'code'
            optionstring = code.group(1)
            line = ''
        
        # If the codeblock has ended, process it
        if line.startswith('@'):
            blockoptions = get_options(optionstring)
            
            document_text, code_text = codeprocessor.process_code(block, blockoptions)
            
            pyfile.write(code_text)
            outfile.write(document_text)
            block = ''
            state = 'text'
            line = ''
    
        # If processing a code block, store the block for processing
        if state == 'code':
            block = block + line
            
        # If processing text, copy the line to the output file 
        if state == 'text':
            outfile.write(line)
    
    # Done processing the file, save extracted code and tell the user what has happened
    pyfile.close()
    codefile.close()
    
    print 'Output written to', outfile_fname
    print 'Code extracted to', pyfile_fname


if __name__ == "__main__":
    if len(sys.argv)==1:
        print "This is Pweave, enter Pweave -h for help"
        sys.exit()
    
    # Command line options
    parser = OptionParser(usage="%prog [options] sourcefile", version="%prog 0.12")
    parser.add_option("-f", "--format", dest="format", default='sphinx',
                      help="The ouput format: 'sphinx' (default), 'rst' or 'tex'")
    parser.add_option("-m", "--matplotlib", dest="mplotlib", default='true',
                      help="Do you want to use matplotlib true (default) or false")
    parser.add_option("-g", "--figure-format", dest="figfmt",
                      help="Figure format for matplolib graphics: "
                           "Defaults to 'png' for rst and Sphinx html, " 
                           "and 'pdf' for tex documents ")
    parser.add_option("-d", "--figure-directory", dest="figdir", default = 'images/',
                      help="Directory path for matplolib graphics: Default 'images/'")
    (options, args) = parser.parse_args()
    infile = args[0]
    run_pweave()


