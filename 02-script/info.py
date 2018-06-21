#!/usr/bin/python

import lldb
import commands
import optparse
import shlex

def info(debugger, command, result, internal_dict):
    print "\033[034m[check] target list\033[0m\n"
    debugger.HandleCommand("ta l")
    print "\n-----\n"
    print "\033[034m[check] breakpoint list\033[0m\n"
    debugger.HandleCommand("br l")
    print "\n-----\n"
    print "\033[034m[show] argument\033[0m\n"
    debugger.HandleCommand("settings show target.run-args")

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand("command script add -f info.info info")
    print 'The "info" python command has been installed and is ready for use.'
