## we have a python interpreter
## we have a program/script

## python script => byte code (mostly hidden) => python virtual machine (python VM)     || byte code -mostly hidden but when you do things like import etc, then it's visible  || this byte code is different from the byte code concept in Java

## Step 1:  compile to byte code (low level and platform independent)  | tech jargon for interpretation (python is an interpreted language)
##           byte code runs faster (than the script, why?)
##          .pyc    ---- compiled python (frozen binaries)
##            __pycache__  (a system folder for python internal usage which it generates itself)

##                         Source Change & Python Version
                                 name.cpython-38.pyc       || filename: name.py   |python version: 3.8 |

                                 => works only for imported files
                                 => not for top level files 


_____________________________________________________________________________________________________________________________

## Python Virtual Machine (PVM)
=> code loop to iterate byte code
=> runtime engine
=> also known as python interpreter



** Byte Code is NOT machine code **

=> byte code is python specific interpretation
=> cpython (standard implementation), jyhton (also called as Jpython), Iron Python, Stackless, PyPy