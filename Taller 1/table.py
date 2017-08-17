import sys
import pandas as pd

name = sys.argv[1]
titles = sys.argv[2:]

df = pd.read_csv(name)

if titles[0] == "all":
    titles = df.keys()
    wanted = df.as_matrix()
else:
    wanted = df[titles].as_matrix()

def printRow(values, bold = False):
    string = ""
    last = len(values) - 1
    for (i, item) in enumerate(values):
        if i != last:
            if bold:
                string += r"\textbf{%s} & "%item
            else:
                string += "%s & "%item
        else:
            if bold:
                string += r"\textbf{%s} \\"%item
            else:
                string += r"%s \\"%item
    string = string.replace("%", r"\%")
    return string + "\n"

string = printRow(titles, True)
string += r"\hline" + "\n"
for row in wanted:
    string += printRow(row)
string += r"\hline" + "\n"

base = r"""
\begin{table}[h]
\centering
\begin{tabular}{%s}
\hline
%s
\end{tabular}
\end{table}
"""%("c"*len(titles), string)

print(base)
