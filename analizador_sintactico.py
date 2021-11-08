import json

operators = {'=' : 'Assignment op','+' : 'Addition op','-' : 'Subtraction op','/' : 'Division op','*' : 'Multiplication op','<' : 'Lessthan op','>' : 'Greaterthan op' }
operators_key = operators.keys()

data_type = {'int' : 'integer type', 'float': 'Floating point' , 'char' : 'Character type', 'long' : 'long int' }
data_type_key = data_type.keys()

punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma' }
punctuation_symbol_key = punctuation_symbol.keys()

identifier = { }
identifier_key = identifier.keys()

symbol_table = {}

with open('tokens.json', 'r') as openfile:
    program = json.load(openfile)
    
    count = 0
    for line in program:
        count += 1
        #print('Line# ', count, '\n')
        
        if(line[-1] not in punctuation_symbol_key):
            #print('Error al final de la linea #', count, 'No se usaron los simbolos de puntuación correctos \n')
            break
        if(line[0] not in identifier_key and line[0] not in data_type_key):
            #print('Error al principio de la linea #', count, 'No se reconoce la variable o el tipo de datos')
            break
        if line[0] in data_type_key:
            if line[1] not in identifier:
                identifier[line[1]] = 'id'
                identifier_key = identifier.keys()
                symbol_table[line[1]] = line[0]
                
        first_id = False
        for token in line:
            if token in identifier.keys():
                if first_id == True:
                    #print('Error, se esperaba un signo de asignacion')
                    break
                first_id = True
            elif first_id == True:
                first_id = False
        
