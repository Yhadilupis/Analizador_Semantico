import ply.yacc as yacc
from analizador_lex import tokens  

parse_errors = []


def p_program(p):
    '''program : statement
               | statement program'''
    if len(p) == 2:
        p[0] = (p[1],)
    else:
        p[0] = (p[1],) + p[2]

#Define reglas gramaticales para la producción
def p_statement(p):
    '''statement : DV
                 | EC
                 | CF
                 | DF'''
    p[0] = p[1]

def p_declaracion_variable(p):
    '''DV : Identificador ASIGNACION Valores'''
    p[0] = ('declaracion_variable', p[1], p[3])

def p_estructura_control(p):
    '''EC : Palabra_reservada_sentencia_if LLAVE_izquierda COND LLAVE_derecha Simbolo_cierre_de_sentencia Corchete_izquierdo CT Corchete_derecho'''
    p[0] = ('Estructura_control', p[2], p[7])

def p_declaracion_funcion(p):
    '''CF : Palabra_reservada_Funcion Identificador PARENTESIS_izquierdo PARENTESIS_derecho Corchete_izquierdo Identificador ASIGNACION Identificador RT Corchete_derecho'''
    p[0] = ('Funciones', p[2], p[9])

def p_ciclo_for(p):
    '''DF : Palabra_reservada_For PARENTESIS_izquierdo Identificador ASIGNACION Valor_numerico COMA Identificador Operador_comparacion Valor_numerico COMA Identificador AUMENTO PARENTESIS_derecho Corchete_izquierdo CT Corchete_derecho'''
    p[0] = ('ciclo_for', {
        'inicializacion': (p[3], p[5]),
        'condicion': (p[7], p[8], p[9]),
        'actualizacion': (p[11], p[12]),
        'cuerpo': p[15]
    })

def p_condicion(p):
    '''COND : Valor_numerico Operador_comparacion Valor_numerico'''
    p[0] = ('condicion', p[1], p[2], p[3])


def p_ct(p): 
    '''CT : PRINT PARENTESIS_izquierdo Valor_numerico PARENTESIS_derecho
          | PRINT PARENTESIS_izquierdo Identificador PARENTESIS_derecho
          | PRINT PARENTESIS_izquierdo Valor_booleano PARENTESIS_derecho '''
    p[0] = ('Print', p[3])

def p_rt(p): 
    '''RT : Palabra_reservada_para_retorno Identificador '''
    p[0] = ('return', p[2])

def p_valores(p):
    '''Valores : Valor_booleano
            | valor_String
            | N'''
    p[0] = p[1]

def p_valor_String(p):
    '''valor_String : String'''
    p[0] = p[1]

def p_numero(p):
    '''N : Valor_numerico'''
    p[0] = p[1]

def p_error(p):
    if p:
        error_message = f"Error de sintaxis en '{p.value}'"
    else:
        error_message = "Se a encontrado un error de sintaxis"
    parse_errors.append(error_message)
 
parser = yacc.yacc() 

def parse(data):
    global parse_errors
    parse_errors = [] 
    result = parser.parse(data)
    if len(parse_errors) > 0:
        return parse_errors
    return result
