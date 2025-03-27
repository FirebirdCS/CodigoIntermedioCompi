from AST import BinOp, Num

class SyntaxAnalyzer:
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
        node = self.expression()
        self.match("EOF")
        print("Análisis sintáctico completado: La estructura es válida.")
        return node

    # expression -> term { (PLUS | MINUS) term }
    def expression(self):
        node = self.term()
        while self.current_token() in ["PLUS", "MINUS"]:
            op = self.current_token()
            self.advance()
            right_node = self.term()
            node = BinOp(op, node, right_node)
        return node

    # term -> factor { (MULT | DIV) factor }
    def term(self):
        node = self.factor()
        while self.current_token() in ["MULT", "DIV"]:
            op = self.current_token()
            self.advance()
            right_node = self.factor()
            node = BinOp(op, node, right_node)
        return node

    # factor -> BINARY_CONST | LPAREN expression RPAREN
    def factor(self):
        tok = self.current_token()
        if tok == "BINARY_CONST":
            value = self.lexemes[self.current]
            self.advance()
            return Num(value)
        elif tok == "LPAREN":
            self.match("LPAREN")
            node = self.expression()
            self.match("RPAREN")
            return node
        else:
            raise SyntaxError("Se esperaba un número binario o '(' en la expresión.")
