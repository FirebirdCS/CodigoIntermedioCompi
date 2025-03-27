import re

class LexicalDict:
    def tokenize(self, code):
        rules = [
            ('BINARY_CONST', r'[01]+'),
            ('PLUS',         r'\+'),
            ('MINUS',        r'-'),
            ('MULT',         r'\*'),
            ('DIV',          r'/'),
            ('LPAREN',       r'\('),
            ('RPAREN',       r'\)'),
            ('SKIP',         r'[ \t]+'),
            ('MISMATCH',     r'.'),
        ]

        tokens = []
        lexemes = []
        rows = []
        columns = []
        
        token_regex = '|'.join('(?P<%s>%s)' % pair for pair in rules)
        master_pattern = re.compile(token_regex)
        
        lines = code.splitlines()
        line_num = 1
        interactive = len(lines) == 1
        
        for line in lines:
            pos = 0
            line_length = len(line)
            while pos < line_length:
                m = master_pattern.match(line, pos)
                if m:
                    token_type = m.lastgroup
                    token_lexeme = m.group(token_type)
                    if token_type == 'SKIP':
                        pos = m.end()
                        continue
                    if token_type == 'MISMATCH':
                        raise RuntimeError(f"Carácter inválido {token_lexeme!r} en la línea {line_num}")
                    tokens.append(token_type)
                    lexemes.append(token_lexeme)
                    rows.append(line_num)
                    columns.append(pos)
                    pos = m.end()
                else:
                    break
            if not interactive:
                tokens.append("NEWLINE")
                lexemes.append("\n")
                rows.append(line_num)
                columns.append(line_length)
            line_num += 1
        
        tokens.append("EOF")
        lexemes.append("EOF")
        rows.append(line_num)
        columns.append(0)
        
        # Impresión de tokens encontrados
        for t, l, r, c in zip(tokens, lexemes, rows, columns):
            print(f"Token: {t:15} Lexema: {repr(l):15} Fila: {r:2} Columna: {c}")
        
        return tokens, lexemes, rows, columns
