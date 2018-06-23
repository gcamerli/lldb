#!/usr/bin/python

import lldb
import commands
import optparse
import shlex
import time

# init function to load the commands
def init(debugger, command, result, internal_dict):
    av = command.split(" ")
    if not len (av) == 3:
        print "\033[34musage\033[0m: insert 3 numbers"
        exit()

    debugger.SetAsync(True)
    debugger.HandleCommand("br s -n main")
    time.sleep(0.2)
    debugger.HandleCommand("run")
    time.sleep(0.2)
    debugger.HandleCommand("br s -l 16 -i 1")
    debugger.HandleCommand("br s -l 19 -o")
    debugger.HandleCommand("br s -l 32")
    debugger.HandleCommand("br s -l 41")
    debugger.HandleCommand("continue")
    time.sleep(0.2)
    debugger.GetSelectedTarget().GetProcess().PutSTDIN(av[0] + '\n')
    time.sleep(0.2)
    debugger.HandleCommand("expr tab[0] = tab[1]")
    debugger.HandleCommand("continue")
    time.sleep(0.2)
    debugger.GetSelectedTarget().GetProcess().PutSTDIN(av[1] + '\n')
    time.sleep(0.2)
    debugger.HandleCommand("expr int $swap = tab[1]")
    debugger.HandleCommand("continue")
    time.sleep(0.2)
    debugger.GetSelectedTarget().GetProcess().PutSTDIN(av[2] + '\n')
    time.sleep(0.2)
    debugger.HandleCommand("expr count = 0; tab[2] = tab[1]; tab[1] = $swap")
    debugger.HandleCommand("continue")
    time.sleep(0.2)
    debugger.HandleCommand("expr tmp = 0; int j = 0; while(j < max){tmp += min[j]; ++j;}")
    debugger.HandleCommand("continue")
    time.sleep(0.2)
    debugger.HandleCommand("expr int k = 0; while(k < max){biggest = (biggest <= min[k])? min[k] : biggest; ++k;}; max = 0")
    debugger.HandleCommand("continue")

# Add the init command to the lldb python interpreter
def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f init.init init')
    print 'The \033[34minit\033[0m python command has been installed and is ready for use.'
