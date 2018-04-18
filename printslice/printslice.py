#######################################################################################
## Script Info:		printslice.py - Class with functions print long list of text with navigations (Arrows)
##
#######################################################################################
## Create Author:	Fausto Branco
## Create Date:		2018-04-03
## Actual Version:  1.0.0
## Description:		
#######################################################################################
## Log Changes:
## Date:            2018-04-03
## Author:          Fausto Branco
## Version:         1.0.0
## Description:     Initial Version
#######################################################################################
import sys
import keypress

int_SizeLimit = 40
int_LineStartPrint = 20

int_posTOP = 0
int_posDOWN = int_posTOP + int_SizeLimit

int_Acao = -1

lst_Print = []
pos_Lista = 0

obj_keypress = keypress.Get_Key()

__version__ = '1.0.0'

class printslice:
    def __init__(self, SizeLimit=40, LineStartPrint=20):
        """
        Desc: Init class with max Size(Lines) to show the list itens and Line on screen to start print
        """
        global int_SizeLimit
        global int_LineStartPrint
        int_SizeLimit = SizeLimit
        int_LineStartPrint = LineStartPrint

    def _print_slice(self, int_Acao, lst_Print, pos_Lista=0):
        global int_posTOP 
        global int_posDOWN
        global int_SizeLimit
        global int_LineStartPrint        
        int_posTOP += int_Acao
        int_posDOWN += int_Acao
        if int_posTOP  < 0:
           int_posTOP = 0
           int_posDOWN = int_posTOP + int_SizeLimit
        if int_posTOP + int_SizeLimit >= len(lst_Print):
           if len(lst_Print) < int_SizeLimit:
              int_posTOP = 0
           else:
              int_posTOP = len(lst_Print) - int_SizeLimit 
           int_posDOWN = len(lst_Print) 
        if pos_Lista == -1:
           int_posTOP = 0
           int_posDOWN = int_posTOP + int_SizeLimit
        elif pos_Lista == 1:
           if len(lst_Print) < int_SizeLimit:
              int_posTOP = 0
           else:
              int_posTOP = len(lst_Print) - int_SizeLimit
           int_posDOWN = int_posTOP + int_SizeLimit
        if int_posDOWN > len(lst_Print):
           int_posDOWN = len(lst_Print)
        #Get Max len of each item
        lst_Maxlength = [max([len(item) for item in lst_Print])]
        str_fmt = ' '.join('{:<%d}' % l for l in lst_Maxlength)
        for idx,i in enumerate(range(int_posTOP, int_posDOWN)):
            sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (int_LineStartPrint + idx + 1, 2, str_fmt.format(lst_Print[i])))
            sys.stdout.flush()

   
    def print_slice(self, lstPrint, posLista=0):
        """
        Desc: print_slice: function to print list, lstPrint = list of itens to show. posLista = first item os list to show
        """
        global lst_Print
        global pos_Lista
        lst_Print = lstPrint
        pos_Lista = posLista
        self._print_slice(0, lst_Print, -1)
        result_Keypress = ''   
        while result_Keypress <> 'Esc':
            result_Keypress = obj_keypress.keypress()
            if result_Keypress == 'Up':
                self._print_slice(-1, lst_Print)
            elif result_Keypress == 'Down':
                self._print_slice(1, lst_Print)
            elif result_Keypress == 'Home':
                self._print_slice(0, lst_Print, -1)
            elif result_Keypress == 'End':
                self._print_slice(0, lst_Print, 1)
            elif result_Keypress == 'Page Up':
                self._print_slice(-10, lst_Print)
            elif result_Keypress == 'Page Down':
                self._print_slice(10, lst_Print)


