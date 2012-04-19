#!/usr/bin/env python
# encoding: utf-8
"""
File Description

File: PBSHelloWorld.py
Created 2012-04-19

Example of running an array job with PBSArrayBatch
"""

import sys, os
from optparse import OptionParser

import PBSArrayBatch

def main(argv):
    """Callable from Command Line"""
    if argv is None:
        argv = sys.argv;
    
    usageStr = \
        """usage: %prog [options] directory 
        
        Hello World PBSArrayBatch Script.
        Set directory to set the job cwd.
        
        """
        
    parser = OptionParser(usage=usageStr)
    parser.add_option('--name', dest='name', default='PBSHelloWorld')
    parser.add_option('--nodes', dest='nodes', default='1')
    (options, args) = parser.parse_args(argv[1:])
     
    if len(args) == 1:
        runScripts(args[0], options)
    else:
        parser.print_help()
        sys.exit(2)    

def runScripts(directory, options):
    """Parse and run the script"""
    cmdStr = """
    
    echo $HOSTNAME
    echo $a $b > $outdir/$a.$b.txt
    """
    outdir = os.path.join(directory, 'output')
    name = options.name;
    
    argDict = {'a': ['Hello', 'Goodbye', 'Tschus'],
               'b': ['World', 'Earth'],
               'outdir':[outdir],
               };
    
    JG = PBSArrayBatch.JobGroup(name=name, command=cmdStr,
                                arguments = argDict, nodes=options.nodes);
    
    PBSArrayBatch.build_submission(directory, [JG], nodes=options.nodes);

if __name__ == '__main__':
    sys.exit(main(sys.argv))



