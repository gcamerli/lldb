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
        debugger.HandleCommand("br s -p 'std::cin|tmp /= max|return biggest;'")
        time.sleep(0.2)
        debugger.HandleCommand("continue")
        time.sleep(0.2)
        debugger.HandleCommand("expr -- $rsi -= 4")
        time.sleep(0.2)
        debugger.HandleCommand("continue")
        debugger.PutSTDIN(target[0])
        #time.sleep(0.2)
        #debugger.HandleCommand("continue")
        #time.sleep(0.2)
        #debugger.GetSelectedTarget().GetProcess().PutSTDIN(args[1]+'\n')
	#time.sleep(0.2)
	#debugger.HandleCommand("expr -- $rsi += 4")
	#time.sleep(0.2)
	#debugger.HandleCommand("continue")
	#time.sleep(0.2)
	#debugger.GetSelectedTarget().GetProcess().PutSTDIN(args[2]+'\n')
	#time.sleep(0.2)
	#debugger.HandleCommand("expr -- count = 0")
	#time.sleep(0.2)
	#debugger.HandleCommand("continue")
	#time.sleep(0.2)
	#debugger.HandleCommand("expr -- tmp = min[0] + min[1] + min[2]")
	#time.sleep(0.2)
	#debugger.HandleCommand("continue")
	#time.sleep(0.2)
	#debugger.HandleCommand("expr -- biggest = ((min[0] >= min[1]) ? min[0] : (min[1] >= min[2] ? min[1] : min[2]))")
	#time.sleep(0.2)
	#debugger.HandleCommand("continue")

# Add the init command to the lldb python interpreter
def __lldb_init_module(debugger, internal_dict):
        debugger.HandleCommand('command script add -f init.init init')
        print 'The "init" python command has been installed and is ready for use.'
