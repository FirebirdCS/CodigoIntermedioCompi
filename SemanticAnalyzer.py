class SemanticAnalyzer:
    def __init__(self, tokens, lexemes):
        self.tokens = tokens
        self.lexemes = lexemes
        self.current = 0

    def current_token(self):
        if self.current < len(self.tokens):
            return self.tokens[self.current]
        return None

    def advance(self):
        self.current += 1

    def match(self, token_type):
        if self.current_token() == token_type:
            self.advance()
        else:
            raise SyntaxError(f"Se esperaba {token_type} pero se encontró {self.current_token()}.")

    def parse(self):
        result_type = self.expression()
        self.match("EOF")
        print("Análisis semántico completado: La operación es semánticamente válida.")
        return result_type

    # expression -> term { (PLUS | MINUS) term }
    def expression(self):
        left_type = self.term()
        while self.current_token() in ["PLUS", "MINUS"]:
            op = self.current_token()
            self.advance()
            right_type = self.term()
            if left_type != right_type:
                raise Exception(f"Error semántico: No se pueden combinar tipos diferentes con '{op}': {left_type} y {right_type}.")
            left_type = left_type
        return left_type

    # term -> factor { (MULT | DIV) factor }
    def term(self):
        left_type = self.factor()
        while self.current_token() in ["MULT", "DIV"]:
            op = self.current_token()
            self.advance()
            right_type = self.factor()
            if left_type != right_type:
                raise Exception(f"Error semántico: No se pueden combinar tipos diferentes con '{op}': {left_type} y {right_type}.")
            left_type = left_type
        return left_type

    # factor -> BINARY_CONST | LPAREN expression RPAREN
    def factor(self):
        tok = self.current_token()
        if tok == "BINARY_CONST":
            self.advance()
            return "bin"
        elif tok == "LPAREN":
            self.match("LPAREN")
            expr_type = self.expression()
            self.match("RPAREN")
            return expr_type
        else:
            raise Exception("Error semántico: Se esperaba un número binario o '(' en la expresión.")
