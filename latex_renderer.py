#%%

"""
Renders pyomo constraints as latex
"""

__author__ = "Rahul Kakodkar"
__copyright__ = "Me"
__credits__ = ["Rahul Kakodkar"]
__license__ = "Open"
__version__ = "1.0.0"
__maintainer__ = "Rahul Kakodkar"
__email__ = "cacodcar@tamu.edu"
__status__ = "Production"

import inspect
import IPython.display 




def eqn_latex_render(constraint_rule, latex_alias_dict:dict= {}) -> str:
    """renders a string for equation in latex format

    Args:
        constraint_rule (function, optional): constraint definition rule. Defaults to {}
        latex_alias_dict (dict): aliases for vaiables, sets, and symbols

    Returns:
        str: string in latex format
    """
    general_dict = {
        '**': '^',
        '*': '.',
        '==': '=',
        '<=': '\leq',
        '>=': '\geq',
        '[': '(',
        ']': ')',
        'exp': 'exp',
        
        }
    
    unsorted_dict_ = {**latex_alias_dict, **general_dict}
    
    
    list_ = [i for i in unsorted_dict_.keys()]
    list_.sort(key = len)
    list_.reverse()

    dict_ = {i: unsorted_dict_[i] for i in list_}
    str_ = inspect.getsource(constraint_rule).split('return ')[1].split('\n')[0]
    for key in dict_.keys():
        str_ = str_.replace(key, dict_[key])
    print('\\begin{equation}\n')
    print(str_+ '\n')
    print('\\end{equation}\n')
    IPython.display.display(IPython.display.Math(str_))
    return str_




def constraint_rule(instance, t):
    """example constraints
    """
    return instance.var1[t] <= instance.var2[t] + instance.var3[t]

latex_alias_dict = {
    'instance.':'',
    'variable_in_pyomo': 'alias_in_latex_format',
    'var1': 'X',
    'var2': 'Y',
    'var3': 'Z',
    }


eqn_latex_render(constraint_rule = constraint_rule, latex_alias_dict= latex_alias_dict)
    
# %%
