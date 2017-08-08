import json
categories = ['Motion', 'Looks', 'Sound', 'Pen', 'Events', 'Control', 'Sensing', 'Operators', 'Data', 'More Blocks', 'Parameter', 'List', 'Exension'] #Typo is in the standard :P
colordict = {}
for i in categories:
	colordict[i] = '0x' + raw_input(i + ' color preference? (hexadecimal format without #) ')
open('scratch.colors', 'w+').write(json.dumps(colordict))
