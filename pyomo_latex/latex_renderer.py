"""
Renders pyomo constraints as latex
"""

__author__ = "Rahul Kakodkar"
__copyright__ = "Rahul Kakodkar"
__credits__ = ["Rahul Kakodkar"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Rahul Kakodkar"
__email__ = "cacodcar@tamu.edu"
__status__ = "Production"

import inspect



def latex_cons(constraint_rule, latex_alias_dict:dict= {}) -> str:
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
    print('\\begin{equation}')
    print(str_)
    print('\\end{equation}')

    return 
