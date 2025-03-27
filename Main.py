from LexicalDict import LexicalDict
from SemanticAnalyzer import SemanticAnalyzer
from SyntaxAnalyzer import SyntaxAnalyzer
from IntermediateCodeGenerator import IntermediateCodeGenerator

if __name__ == '__main__':
    code = input("Ingrese una operación binaria (con números binarios, operadores [+ - * /] y paréntesis):\n")
    
    # Fase de tokens
    lexer = LexicalDict()
    tokens, lexemes, _, _ = lexer.tokenize(code)
    print("\nTokens generados:", tokens, "\n")

    
    # Fase de análisis sintáctico
    print("Iniciando análisis sintáctico...\n")
    syntax_analyzer = SyntaxAnalyzer(tokens, lexemes)
    try:
        ast_node = syntax_analyzer.parse()
    except Exception as e:
        print("Error sintáctico:", e)
        exit(1)

    # Fase de análisis semántico
    print("Iniciando análisis semántico...\n")
    semantic_analyzer = SemanticAnalyzer(tokens, lexemes)
    try:
        semantic_analyzer.parse()
    except Exception as e:
        print("Error semántico:", e)
        exit(1)
    print("Análisis semántico completado correctamente.\n")
    
    # Fase de generación de código intermedio
    print("Iniciando generación de código intermedio...\n")
    code_generator = IntermediateCodeGenerator()
    result_temp = code_generator.generate_node(ast_node)
    tac_code = code_generator.get_code()
    
    print("Código intermedio generado:")
    for instr in tac_code:
        print(instr)
