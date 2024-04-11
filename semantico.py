import re

variables = []
functions = []

expresion_regex = re.compile(r'{([^{}]+)}')
numero_regex = re.compile(r'^[+-]?\d*\.?\d+$')

def ejecutar(data, lex):
    resultados = expresion_regex.findall(lex)
    variables.clear()
    functions.clear()
    i = 0
    with open('script.js', 'w') as _:
        pass
    for element in data:
        if element[0] == 'declaracion_variable':
            value_var = ''
            if existe_fun(element[1]):
                with open('script.js', 'w') as _:
                    pass
                return False
            
            variables.append(element[1])          
              
            if element[2] == 'true' or element[2] == 'false':
                value_var = element[2]
            elif numero_regex.match(str(element[2])):  # Verificar si es un número
                value_var = numero_regex.match(str(element[2])).group()
            else:
                value_var = element[2]
                value_var = element[2].replace('*', '"')
    
            codigo = '\n{0} = {1}'.format(element[1], value_var)
            with open('script.js', 'a') as file:
                file.write(codigo)
        elif element[0] == 'ciclo_for':
            init = ''
            init_value = ''
            cond_init = ''
            ope_logico = ''
            cond_value = ''
            aum_var = ''
            aum = ''
            imp = ''
            for key, values in element[1].items():
                if key == 'inicializacion':
                    init = values[0]
                    init_value = values[1]
                elif key == 'condicion':
                    cond_init = values[0]
                    ope_logico = values[1]
                    cond_value = values[2]
                elif key == 'actualizacion':
                    aum_var = values[0]
                    aum = values[1]
                elif key == 'cuerpo':
                    imp = values[1]
            if not existe(imp) or imp == 'true' or imp == 'false':
                if imp == 'true' or imp == 'false':
                    pass
                else:
                    with open('script.js', 'w') as _:
                        pass
                        return False
            
            codigo = '\nfor({0} = {1}; {2} {3} {4}; {5}{6}){{\n\tconsole.log({7});\n}}'.format(init, init_value, cond_init, ope_logico, cond_value, aum_var, aum, imp)
            with open('script.js', 'a') as file:
                file.write(codigo)
        
        elif element[0] == 'Funciones':
            if existe(element[1]):
                with open('script.js', 'w') as _:
                    pass
                return False
            print(element[2][1])
            if not existe(element[2][1]):
                print(True)
                with open('script.js', 'w') as _:
                    pass
                return False
            codigo = '\nfunction {0}(){{\na=b\nconsole.log(a);\n\treturn {1}\n}}'.format(element[1], element[2][1])
            functions.append(element[1])
            with open('script.js', 'a') as file:
                file.write(codigo)
        
        elif element[0] == 'Estructura_control':
            codigo = '\nif({0}){{\n\tconsole.log({1})\n}}'.format(resultados[i], element[2][1])
            with open('script.js', 'a') as file:
                file.write(codigo)
            i+=1
    for fn in functions:
        codigo = '\n{0} ();'.format(fn)
        with open('script.js', 'a') as file:
            file.write(codigo)
    return True
                

def existe(var):
    for element in variables:
        if element == var:
            return True
    return False

def existe_fun(var):
    for element in functions:
        if element == var:
            return True
    return False
