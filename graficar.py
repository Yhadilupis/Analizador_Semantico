import subprocess
import sys
import tkinter as tk
from analizador_lex import analyze
from analizador import parse, parse_errors
from semantico import ejecutar

root = tk.Tk()
root.title("Analizador Sémantico")

# Crear un área de texto para la entrada
text_input = tk.Text(root, height=10, width=50, bg="lightgray", fg="black")
text_input.pack()

output = tk.Text(root, height=10, width=50, bg="black", fg="white")
output.pack()

terminal = tk.Text(root, height=10, width=50)
terminal.pack()

def analizar():
    terminal.delete("1.0", tk.END)
    data = text_input.get("1.0", tk.END)
    lexer_results, errors_found = analyze(data)  # Almacenar resultados y verificar errores
        
    output.delete("1.0", tk.END)
    output.insert(tk.END, "Resultados del Análisis Léxico:\n")
    for result in lexer_results:
        output.insert(tk.END, result + '\n')
        
    if len(errors_found) > 0:
        for error in errors_found:
            output.insert(tk.END, error + '\n')
    
    if errors_found:
        output.insert(tk.END, "\nSe encontraron errores léxicos. Análisis sintáctico detenido.\n")
    else:
        output.insert(tk.END, "\nRealizando al Análisis Sintáctico...\n")
        parser_result = parse(data)  # Realiza el análisis sintáctico solo si no hay errores léxicos
        if parse_errors:  # Si hay errores de sintaxis
            for error in parse_errors:
                output.insert(tk.END, error + '\n')
        else:
            output.insert(tk.END, str(parser_result) + '\n')
            if ejecutar(parser_result, data):
                try:
                    ruta_archivo = 'script.js'

                    if sys.platform.startswith('win'):
                        proceso = subprocess.Popen(['node', ruta_archivo], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

                    for line in iter(proceso.stdout.readline, b''):
                        terminal.insert(tk.END, line.decode(sys.stdout.encoding))
                except:
                    pass
            else:
                output.insert(tk.END, 'Error al ejecutar el archivo')



analyze_button = tk.Button(root, text="Analizar", command=analizar)
analyze_button.pack()

root.mainloop()