#!/usr/bin/python

import os
import lldb
import commands
import optparse
import shlex

# pwd function
def cwd(debugger, command, result, internal_dict):
    print >> result, (commands.getoutput('/bin/pwd'))

# Add the pwd command to the lldb python interpreter 
def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f cwd.cwd cwd')
    print 'The "cwd" python command has been installed and is ready for use.'
