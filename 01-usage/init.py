#!/usr/bin/python

import lldb
import commands
import optparse
import shlex
import time

# init function to load the commands
def init(debugger, command, result, internal_dict):
    target = debugger.GetSelectedTarget()
    
    debugger.SetAsync(True)
    debugger.HandleCommand("br s -n main")
    time.sleep(0.2)
    debugger.HandleCommand("run")
    time.sleep(0.2)

# Add the init command to the lldb python interpreter
def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f init.init init')
    print 'The \033[34minit\033[0m python command has been installed and is ready for use.'
