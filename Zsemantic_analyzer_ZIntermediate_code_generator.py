from Zparser import ast
import symtable

# First Section: Semantic Analysis
symbol_table = symtable.symtable()  # Create symbol table
if ast.semantic_analysis(symbol_table):
    print("Semantic Analysis passed!")
else:
    print("Semantic Analysis failed!")

# Second Section: Intermediate Code Generation
code = ast.generate_intermediate_code()
if code:
    print("Intermediate Code generated!")
    print(code)
else:
    print("Intermediate Code generation failed!")
