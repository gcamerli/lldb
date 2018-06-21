# **LLDB**

42 (Paris)

### **Description**

**LLDB** is a next generation, high-performance **debugger**. It is built as a set of reusable components which highly leverage existing libraries in the larger **LLVM** Project, such as the Clang expression parser and LLVM disassembler.

The purpose of this project is to discover some debugging techniques with **LLDB**.

### **Requirements**

+ lldb

### **Config**

To customize your lldb prompt, place the `.lldbinit` file in the `$HOME` dir:

```shell
$ cp 00-init/.lldbinit $HOME
```

### **Usage**

Execute the `run.sh` script and from the lldb prompt run:

```shell
(lldb) command script import 01-usage/init.py
```

This action will bind the `test/source.cpp` file to the lldb debugger.

### **Script**

To load more scripts inside the lldb prompt, re-execute for each file:

```shell
(lldb) command script import _[path/file.py]_
```

Happy hacking!

### **Doc**

Check the official [doc](https://lldb.llvm.org/).

### **License**

This work is published under the terms of [42 Unlicense](https://github.com/gcamerli/42unlicense).
