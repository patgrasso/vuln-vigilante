import sys
from pycparser import parse_file, c_ast

ast = parse_file(sys.argv[1], use_cpp=True,
  cpp_args=r"-Ithird_party/pycparser/utils/fake_libc_include")


new_stack = lambda main_name, main_params: [
  c_ast.FuncCall(
    c_ast.ID(main_name),
    c_ast.ExprList([ c_ast.ID(param.name) for param in main_params ])
  )
]

class Program:

  do_not_yield = (
    c_ast.FuncDecl,
    c_ast.Decl,
    c_ast.FuncDef,
    c_ast.Compound,
  )

  def __init__(self, ast):
    self.ast = ast
    self.func_defs = { tld.decl.name: tld
                       for tld in ast
                       if isinstance(tld, c_ast.FuncDef) }
    self.main = None
    if "main" in self.func_defs:
      self.main = self.func_defs["main"]

      self.curr_node = None
      self.call_stack = []
      self.context = {}

  def __iter__(self, node=None, stack=None):
    node = node if node is not None else self.main
    stack = stack if stack is not None else new_stack(
        node.decl.name, node.decl.type.args.params)

    # jump to function
    if isinstance(node, c_ast.FuncCall):
      if node.name.name in self.func_defs:
        for item in self.__iter__(self.func_defs[node.name.name], stack + [node]):
          yield item
      else:
        yield stack, node.name

    # dig deeper
    #elif isinstance(node, c_ast.Compound):
    #  for child in node:
    #    for grandchild in self.__iter__(child, stack):
    #      yield grandchild

    elif isinstance(node, self.do_not_yield):
      for child in node:
        yield from self.__iter__(child, stack)

    # yield this node
    else:
      yield stack, node



  def on_node(self, node, call_stack):
    pass



def walk(node, level=0):
  if hasattr(node, "children"):
    for child_name, child in node.children():
#      name = "<" + child.__class__.__name__ + ">"
      name = ""
      if hasattr(child, "name"):
        name = child.name
        if hasattr(name, "name"):
          name = name.name
      elif hasattr(child, "declname"):
        name = child.declname
      elif hasattr(child, "value"):
        name = child.value
      elif hasattr(child, "names"):
        name = child.names
      elif hasattr(child, "quals"):
        name = child.quals
      print(" "*level*2, type(child).__name__ + ":", name)
      walk(child, level+1)


nw = Program(ast)
walk(ast.ext[-1])
#it = iter(nw)

