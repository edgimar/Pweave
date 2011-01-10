#!/usr/bin/python

# Pweave, Literate programming tool for Python 
# ============================================
# 
# :Author: Matti Pastell <matti.pastell@helsinki.fi
# :Website: http://mpastell.com
# Version: 0.12

import sys
import StringIO
import re
from optparse import OptionParser
import os
exec_namespace = {} # global (and local) namespace for exec()'ed code

# A function for parsing options
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
    return(echo, results, evaluate, fig, width, caption, term)

def exec_code(code_as_string):
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

def run_pweave():
    # Is matplotlib used? 
    
    if options.mplotlib.lower() == 'true':
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    
    # Format specific options for tex or rst
    
    if format == 'tex':
        codestart = '\\begin{verbatim}' 
        codeend = '\end{verbatim}\n'
        outputstart = '\\begin{verbatim}' 
        outputend = '\end{verbatim}\n' 
        codeindent = ''
        figfmt = '.pdf'
        ext = 'tex'
    if format == 'rst':
        codestart = '::\n\n' 
        codeend = '\n\n'
        outputstart = '::\n\n' 
        outputend = '\n\n' 
        codeindent = '  '
        figfmt = '.png'
        ext = 'rst'
    if format == 'sphinx':
        codestart = '::\n\n' 
        codeend = '\n\n'
        outputstart = '::\n\n' 
        outputend = '\n\n' 
        codeindent = '  '
        figfmt = '.png'
        sphinxtexfigfmt = '.pdf'
        ext = 'rst'
    
    # Override the default fig format with command line option
    
    if options.figfmt > 0:
        figfmt = '.' + options.figfmt
    
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
    nfig = 1
    allcode = ''
    imgdir = options.figdir
    
    # Create figure directory if it doesn't exist
    if os.path.isdir(imgdir) == False:
        os.mkdir(imgdir)
    
    

    
    # Process the whole text file with a loop
    
    for line in lines:
    # If start of code block, set state as block and get the options
        code = re.search('^<<(.|)+>>=$', line.strip())
        if code > 0:
            state = 'code'
            optionstring = line[2:len(line.strip())-3]
            line = ''
    
    # The codeblock has ended, less process it
        if line.startswith('@'):
            #Get options 
            echo, results, evaluate, fig, width, caption, term = get_options(optionstring)
    
            #Output in doctests mode
            #print dtmode
            if term:
                outfile.write('\n')
                if format=="tex": outfile.write(codestart)  
                #Write output to a StringIO object
                #loop trough the code lines
                for x in block.splitlines():
                    outfile.write('>>> ' + x)
                    result = exec_code(x)
                    
                    if len(result) > 0:
                        outfile.write(result)
                result = ''        
                outfile.write(codeend)
            else:
                #include source?
                if echo==True:
                    outfile.write(codestart)
                    for x in block.splitlines():
                        outfile.write(codeindent + x + '\n')
                    outfile.write(codeend)
                
                #Evaluate the code?
                if evaluate==True:
                    if fig:
                        #A placeholder for figure options
                        #import matplotlib
                        #matplotlib.rcParams['figure.figsize'] = (6, 4.5)
                        pass
                    
                    result = exec_code(block).splitlines()
            
            #If we get results they are printed
            if len(result) > 0:
                #TODO: fix -- if results != "verbatim" and !=rst and !=tex, 
                #      then indent isn't defined and code will break.
                if results == "verbatim":
                    outfile.write(outputstart)
                    indent = codeindent
                
                if results == "rst" or results == "tex":
                    indent = ''
                
                for x in result:
                    outfile.write(indent + x)
                outfile.write('\n')
                
                if results == "verbatim":
                    outfile.write(outputend)
                result = ''
            
            #Save and include a figure?
            if fig:
                figname = imgdir + 'Fig' +str(nfig) + figfmt
                plt.savefig(figname, dpi = 200)
                #savefig(figname)
                if format == 'sphinx':
                    figname2 = imgdir + 'Fig' +str(nfig) +  sphinxtexfigfmt
                    plt.savefig(figname2)
                plt.clf()
                if format == 'rst':
                    if caption > 0:
                        #If the image has a caption, use Figure directive
                        outfile.write('.. figure:: ' + figname + '\n')
                        outfile.write('   :width: ' + width + '\n\n')
                        outfile.write('   ' + caption + '\n\n')
                    else:
                        outfile.write('.. image:: ' + figname + '\n')
                        outfile.write('   :width: ' + width + '\n\n')
                if format == 'sphinx':
                    if caption > 0:
                        outfile.write('.. figure:: ' + imgdir + 'Fig' + str(nfig)  + '.*' + '\n')
                        outfile.write('   :width: ' + width + '\n\n')
                        outfile.write('   ' + caption + '\n\n')
                    else:
                        outfile.write('.. image:: ' + imgdir + 'Fig' + str(nfig)  + '.*' + '\n')
                        outfile.write('   :width: ' + width + '\n\n')
                if format == 'tex':
                    if caption > 0:
                        outfile.write(r'\begin{figure}' + '\n')
                        outfile.write('\includegraphics{'+ figname + '}' + '\n')
                        outfile.write('\caption{' + caption + '}' + '\n')
                        outfile.write('\end{figure}' + '\n')
                    else:
                        outfile.write('\includegraphics{'+ figname + '}\n\n')
    
                nfig = nfig +1
            allcode = allcode + block
            block = ''
            state = 'text'
            line = ''
    
    # If processing a code block, store the block for processing
    
        if state == 'code':
            block = block + line
    # If processing text, print it as it is 
    
        if state == 'text':
            outfile.write(line) 
    
    # Done processing the file, save extracted code and tell the user what has happened
    pyfile.write(allcode)
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
                      help="Figure format for matplolib graphics: Defaults to 'png' for rst and Sphinx html documents and 'pdf' for tex")
    parser.add_option("-d", "--figure-directory", dest="figdir", default = 'images/',
                      help="Directory path for matplolib graphics: Default 'images/'")
    (options, args) = parser.parse_args()
    format = options.format
    infile = args[0]
    run_pweave()


