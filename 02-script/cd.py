#!/usr/bin/python

import os
import lldb
import commands
import optparse
import shlex

# cd function
def cd(debugger, command, result, internal_dict):
    debugger.HandleCommand('platform settings -w %s' % command)

# Add the cd command to the lldb python interpreter 
def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f cd.cd cd')
    print 'The "cd" python command has been installed and is ready for use.'
