# PrintSlice

Class with functions print long list of text with navigations (Arrows)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Developed and tested in Linux Ubuntu and Python 2.7


### Installing

A step by step series of examples that tell you have to get a development env running

1. Create a folder called "printslice" inside the folder of your project.
2. Copy the printslice.py and `__init__.py` files to the printslice folder
3. Do class import for your project normally.

* If the import is successful, a file called printslice.pyc must be created, this file (compiled python file) must be maintained.

## Functions

### Creating a object / instance
printslice(SizeLimit=40, LineStartPrint=20))
Description: Init class with max Size(Lines) to show the list itens and Line on screen to start print

### print_slice

print_slice(lstPrint, posLista=0)

Description: print_slice: function to print list, lstPrint = list of itens to show. posLista = first item os list to show

**lstPrint**: list of itens to show
**posLista**: first item os list to show

Information:
Press Home to go to begin of list
Press End to go to end of list
Press PgUp to step 10 lines Up
Press PgDown to step 10 lines down
Arrows:
    Up: Move one line up
    Down: Move one line down
    
Return: None
              
## Deployment

Additional notes about how to deploy this on a live system:
Para deploy em ambiente de live:
1) Create a folder called "checkbox" inside the folder of your project.
2) Copy the checklist.pyc and `__init__.pyc` files to the checkbox folder

Note: Unless you really have experience, do not install directly on /usr/local/lib/python2.7/dist-packages

For next versions will be available installation by setup or pip.

## Examples of use

```
lst_Print = []        
for i in range(500):
    lst_Print.append('Texto: ' + str(i) + ' Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

import printslice
objPrint = printslice.printslice(20, 20)

print "\033c"
objPrint.print_slice(lst_Print)

    
```
[![](https://github.com/faustobranco/printslice/blob/master/Capture.PNG)](https://github.com/faustobranco/printslice/blob/master/Capture.PNG)

## Versioning
```
=======================================================================================
== Log Changes:
== Date:            2018-04-03
== Author:          Fausto Branco
== Version:         1.0.0
== Description:     Initial Version
=======================================================================================
```
## Authors
```
=======================================================================================
== Script Info:		printslice.py - Class with functions print long list of text with navigations (Arrows)
==
=======================================================================================
== Create Author:	Fausto Branco
== Create Date:		2018-04-03
== Actual Version:  1.0.0
== Description:		
=======================================================================================
== Log Changes:
== Date:            2018-04-03
== Author:          Fausto Branco
== Version:         1.0.0
== Description:     Initial Version
=======================================================================================
```
## License



