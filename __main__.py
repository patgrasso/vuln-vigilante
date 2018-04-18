import sys

third_party = [
  "./third_party/pycparser/build/lib"
]
for lib in third_party:
  sys.path.insert(0, lib)

import parse_c
