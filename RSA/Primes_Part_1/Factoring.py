#python3 -m venv myenv
#source myenv/bin/activate

from sympy import factorint

N = 510143758735509025530880200653196460532653147
factors = factorint(N)
print(factors)
