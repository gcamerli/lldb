#!/usr/bin/python

import lldb
import commands
import optparse
import shlex

def reverse(debugger, command, result, internal_dict):
    target = debugger.GetSelectedTarget()
    if not target:
        print "error: invalid target, create a target using the 'target create' command."
    else:
        print "FT_"+str(target)[::-1]

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f reverse.reverse reverse')
    print 'The \033[34mreverse\033[0m python command has been installed and is ready for use.'
