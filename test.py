import numpy
from openpyxl import load_workbook
import numpy as np

wb = load_workbook('database.xlsx')

# in ra gia tri trong mot hang////
ws = wb['Tom']
m = []
for a in ws.values:
    m.append(a)
print(np.array(m))
