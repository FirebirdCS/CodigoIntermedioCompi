from AST import BinOp, Num

class IntermediateCodeGenerator:
    def __init__(self):
        self.temp_count = 0    
        self.code = []       

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate_node(self, node):
        if isinstance(node, BinOp):
            left = self.generate_node(node.left)
            right = self.generate_node(node.right)
            temp = self.new_temp()
            self.code.append(f"{temp} = {left} {node.op} {right}")
            return temp
        elif isinstance(node, Num):
            return node.value
        else:
            raise Exception("Nodo no reconocido en la generación de código.")

    def get_code(self):
        return self.code
