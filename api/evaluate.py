import sys
import re

import api.functions as functions
from api.variables import *
from api.console import *
from api.open import *

console = Console()

def evaluate(expression):
    # Перестановка всех переменных на их значения
    for var in variables:
        expression = expression.replace(var, str(variables[var]))
    
    # Перестановка всех пользовательский функций на их значения
    for func in user_functions:
        matches = re.findall(f"{func}\((.*?)\)", expression)
        for match in matches:
            args = match.split(",")

            if len(args) != len(user_functions[func]["args"]):
                console.error(language_dictionary[language]["errors"][3][0] + f"{func}" + language_dictionary[language]["errors"][3][1] + f"{line_number}|'{old_line}'")
                console.info(language_dictionary[language]["exit_code"][0] + "-3" + language_dictionary[language]["exit_code"][1])
                console.show()
                sys.exit()
            
            subs = dict(zip(user_functions[func]["args"], args))
            body = user_functions[func]["body"]
            for arg in subs: body = body.replace(arg, subs[arg])
            expression = expression.replace(f"{func}({match})", f"({body})")
    
    # Перестановка всех функций в выражениях на значения
    for func in dir(functions):
        if not func.startswith("_"):
            expression = expression.replace(func, f"functions.{func}")
    
    # Проверка на ошибок и их вывод
    # НУЖНО РЕАЛИЗОВАТЬ ОШИБКУ НА НЕПРАВИЛЬНОЕ НАЗВАНИЕ!
    try:
        result = eval(expression)
    except ZeroDivisionError:
        console.error(language_dictionary[language]["errors"][5] + f"{line_number}|'{old_line}'")
        console.info(language_dictionary[language]["exit_code"][0] + "-5" + language_dictionary[language]["exit_code"][1])
        console.show()
        sys.exit()
    except TimeoutError:
        console.error(language_dictionary[language]["errors"][6] + f"{line_number}|'{old_line}'")
        console.info(language_dictionary[language]["exit_code"][0] + "-6" + language_dictionary[language]["exit_code"][1])
        console.show()
        sys.exit()
    except MemoryError:
        console.error(language_dictionary[language]["errors"][7] + f"{line_number}|'{old_line}'")
        console.info(language_dictionary[language]["exit_code"][0] + "-7" + language_dictionary[language]["exit_code"][1])
        console.show()
        sys.exit()
    except ArithmeticError:
        console.error(language_dictionary[language]["errors"][8] + f"{line_number}|'{old_line}'")
        console.info(language_dictionary[language]["exit_code"][0] + "-8" + language_dictionary[language]["exit_code"][1])
        console.show()
        sys.exit()
    except SyntaxError:
        console.error(language_dictionary[language]["errors"][4] + f"{line_number}|'{old_line}'")
        console.info(language_dictionary[language]["exit_code"][0] + "-4" + language_dictionary[language]["exit_code"][1])
        console.show()
        sys.exit()
    
    return result
