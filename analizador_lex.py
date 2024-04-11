import ply.lex as lex
from ply.lex import LexError

lexical_errors = []

tokens = [
    'Palabra_reservada_For', 'PRINT','Palabra_reservada_Funcion', 'Valor_booleano',
    'Palabra_reservada_sentencia_if', 'Identificador', 'ASIGNACION', 'String',
    'Valor_numerico', 'Simbolo_cierre_de_sentencia', 'PARENTESIS_izquierdo',
    'PARENTESIS_derecho', 'LLAVE_izquierda', 'LLAVE_derecha', 'Operador_comparacion',
    'Palabra_reservada_para_retorno', 'COMA', 'Corchete_izquierdo', 'Corchete_derecho', 'AUMENTO'
]

#Reglas
t_ASIGNACION = r'='
t_Simbolo_cierre_de_sentencia = r'\!'
t_PARENTESIS_izquierdo = r'\('
t_PARENTESIS_derecho = r'\)'
t_LLAVE_izquierda = r'\{'
t_LLAVE_derecha = r'\}'
t_Operador_comparacion = r'==|<=|>=|<|>'
t_COMA = r','
t_Corchete_izquierdo = r'\['
t_Corchete_derecho = r'\]'
t_AUMENTO = r'\+\+|--'


def t_Palabra_reservada_For(t):
    r'F'
    return t

def t_Palabra_reservada_sentencia_if(t):
    r'¡si'
    return t

def t_Palabra_reservada_Funcion(t):
    r'fun'
    return t

def t_Palabra_reservada_para_retorno(t):
    r'return'
    return t

def t_PRINT(t):
    r'Print'
    return t

def t_Identificador(t):
    r'[a-z]+'
    if t.value == 'F':
        t.type = 'Palabra_reservada_For'
    elif t.value == '¡si':
        t.type = 'Palabra_reservada_sentencia_if'
    elif t.value == 'fun':
        t.type = 'Palabra_reservada_Funcion'
    elif t.value == 'return':
        t.type = 'Palabra_reservada_para_retorno'
    elif t.value == 'Print':
        t.type = 'PRINT'
    elif t.value == 'true' or t.value == 'false':
        t.type = "Valor_booleano"
    return t


def t_Valor_booleano(t):
    r'true|false'
    return t


def t_String(t):
    r'\*[a-z0-9 ]*\*'
    return t


def t_Valor_numerico(t):
    r'-?\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    message = f"Error léxico: '{t.value[0]}'"
    lexical_errors.append(message)
    t.lexer.skip(1)

lexer = lex.lex() 

#reinicia la lista de errores
def clear_lexical_errors():
    global lexical_errors
    lexical_errors = []
    
def analyze(data):
    lexer.input(data)
    results = []
    clear_lexical_errors()
    try:
        while True:
            tok = lexer.token()
            if not tok:
                break
            results.append(str(tok))
    except LexError as e:
        results.append(f"Error de lexing: {e}")
    return results, lexical_errors