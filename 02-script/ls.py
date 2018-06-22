#!/usr/bin/python

import os
import lldb
import commands
import optparse
import shlex

# ls function
def ls(debugger, command, result, internal_dict):
    print >> result, (commands.getoutput('/bin/ls %s' % command))

# Add the ls command to the lldb python interpreter 
def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f ls.ls ls')
    print 'The \033[34mls\033[0m python command has been installed and is ready for use.'
