import ast
import astor
import copy
import sys

class MutationFinder(ast.NodeVisitor):
    """
    Collects nodes that can be mutated.
    """
    def __init__(self):
        self.mutation_points = []

    def visit_Compare(self, node):
        self.generic_visit(node)
        self.mutation_points.append(('Compare', copy.deepcopy(node),node.lineno,node.col_offset))
    
    def visit_BinOp(self, node):
        self.generic_visit(node)
        self.mutation_points.append(('BinOp', copy.deepcopy(node),node.lineno,node.col_offset))

    #TODO: BoolOp, AugAssign, Constant

    def visit_BoolOp(self, node):
        self.generic_visit(node)
        self.mutation_points.append(('BoolOp', copy.deepcopy(node),node.lineno,node.col_offset))

    
    def visit_AugAssign(self, node):
        self.generic_visit(node)
        self.mutation_points.append(('AugAssign', copy.deepcopy(node),node.lineno,node.col_offset))
    
    def visit_Constant(self, node):
        if isinstance(node.value, (bool, str)):
            self.generic_visit(node)
            self.mutation_points.append(('Constant', copy.deepcopy(node),node.lineno,node.col_offset))

def mutate_node(node):
    """
    Applies a mutation to a single node.
    """
    if isinstance(node, ast.Compare):
        return mutate_compare(node)
    elif isinstance(node, ast.BinOp):
        return mutate_binop(node)
    elif isinstance(node, ast.BoolOp):
        return mutate_boolop(node)
    elif isinstance(node, ast.AugAssign):
        return mutate_augassign(node)
    elif isinstance(node, ast.Constant):
        return mutate_constant(node)
    return node

def mutate_compare(node):
    comparator_map = {
        ast.Eq : ast.NotEq,
        ast.NotEq : ast.Eq,
        ast.Lt : ast.Gt,
        ast.LtE : ast.GtE,
        ast.Gt: ast.Lt,
        ast.GtE: ast.LtE,
        ast.Is : ast.IsNot,
        ast.IsNot: ast.Is,
        ast.In : ast.NotIn,
        ast.NotIn : ast.In  
    }
    new_ops = []
    for op in node.ops:
        if type(op) in comparator_map:
            new_ops.append(comparator_map[type(op)]())
        else:
            new_ops.append(op)
    node.ops = new_ops
    return node

def mutate_binop(node):
    binop_map = {
        ast.Add : ast.Sub,
        ast.Sub : ast.Add,
        ast.Mult : ast.FloorDiv,
        ast.Div : ast.Mult,
        ast.FloorDiv : ast.Mult,
    }
    # new_ops = []
    if type(node.op) in binop_map:
        node.op = binop_map[type(node.op)]()
    return node

def mutate_boolop(node):
    boolp_map = {
        ast.And : ast.Or,
        ast.Or : ast.And
    }
    if type(node.op) in boolp_map:
        node.op = boolp_map[type(node.op)]()
    return node

def mutate_augassign(node):
    augassign_map = { 
        ast.Add : ast.Sub, 
        ast.Sub : ast.Add
    }
    if type(node.op) in augassign_map:
        node.op = augassign_map[type(node.op)]()
    return node

def mutate_constant(node):
    if isinstance(node.value, str):
        node.value += "_makeitlonger"
    elif isinstance(node.value, bool):
        node.value = not node.value
    return node
        
#=====================================================================

def apply_mutation_and_generate_file(original_ast, mutation_point, file_index):
    """
    Applies a single mutation and generates a file for it.
    """
    mutated_ast = copy.deepcopy(original_ast)

    mutation_type, original_node, linenumber, col_offset = mutation_point

    # Find the matching node in the deep-copied AST and apply the mutation
    for node in ast.walk(mutated_ast):
        if (type(node) == type(original_node) and 
            ast.dump(node) == ast.dump(original_node) and 
            node.lineno == linenumber and
            node.col_offset == col_offset):
            print(f"Mutating '{mutation_type}' at line {linenumber}")
            mutate_node(node)
            break

    mutated_code = astor.to_source(mutated_ast)
    filename = f"mutation_{file_index}.py"
    with open(filename, "w") as file:
        file.write(mutated_code)
    print(f"Generated {filename}")
    print("--"*15)

def generate_mutations(source_code):
    original_ast = read_and_parse(source_code)
    finder = MutationFinder()
    finder.visit(original_ast)

    print("=="*20)
    print(f"Found {len(finder.mutation_points)} mutants to mutate")
    print("=="*20)

    for i, mutation_point in enumerate(finder.mutation_points, start=1):
        apply_mutation_and_generate_file(original_ast, mutation_point, i)

def read_and_parse(file_name):
    with open(file_name, "r") as file:
        source_code = file.read()
    return ast.parse(source_code)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        generate_mutations(sys.argv[1])
    else:
        print("Usage: python script.py <source_file.py>")