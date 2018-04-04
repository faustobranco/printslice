lst_Print = []        
for i in range(500):
    lst_Print.append('Texto: ' + str(i) + ' Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

import printslice
objPrint = printslice.printslice(20, 20)

print "\033c"
objPrint.print_slice(lst_Print)

