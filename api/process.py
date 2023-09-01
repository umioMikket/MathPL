import re

from api.variables import *
from api.evaluate import *

console = Console()

def process(line):
    global language

    # Удаление пробелов, комментариев, перестановка знаков
    line = line.strip()
    line = line.replace("^", "**")
    line = re.sub(r"#.*","",line)
    console.info(str(variables))

    # Если линия не начинаеться сразу с комментария, то тогда ее нужно выполнить
    if line and not line.startswith("#"):

        if re.match("^[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*.+$", line):
            # Проверка на переменную
            name, expression = line.split("=", maxsplit=1)
            name = name.strip()
            expression = expression.strip()
            value = evaluate(expression)
            variables[name] = value
        
        elif re.match("^[a-zA-Z_][a-zA-Z0-9_]*\s*\((.*?)\)\s*=\s*.+$", line):
            # Проверка на пользовательскую функцию
            name_args, expression = line.split("=", maxsplit=1)
            name_args = name_args.strip()
            expression = expression.strip()
            name, args = name_args.split("(", maxsplit=1)
            name = name.strip()
            args = args[:-1]
            args = args.split(",")
            args = [arg.strip() for arg in args]
            user_functions[name] = {"args": args, "body": expression}
        
        elif re.match("^print\(.+\)$", line):
            # Проверка на вывод информации
            message = line[6:-1]
            message = message.format(**variables)
            console.info(language_dictionary[language]["message"][0] + message.strip('"') + language_dictionary[language]["message"][1] + f"{line_number}:{old_line}")
        
        elif re.match("^lang\(.+\)$", line):
            # Проверка на смену языка
            message = line[5:-1]
            if message == "eng": language = "eng"
            elif message == "ru": language = "ru"
            else:
                console.error(language_dictionary[language]["errors"][9][0] + f"{line_number}|'{old_line}'")
                console.error(language_dictionary[language]["errors"][9][1])
                console.info(language_dictionary[language]["exit_code"][0] + "-9" + language_dictionary[language]["exit_code"][1])
                console.show()
                sys.exit()
        
        elif re.match("^InfoMathPLang\(\)$", line):
            # Просто как комманда для вывода информации о языке
            console.info(language_dictionary[language]["lang_info"][0])
            console.info(language_dictionary[language]["lang_info"][1])
            console.info(language_dictionary[language]["lang_info"][2])

        else:
            # Если у нас все прошлые проверки были отклонены то тогда пытаемся выввести просто линию с арефметическим действием
            value = evaluate(line)
            console.info(language_dictionary[language]["message"][0] + str(value) + language_dictionary[language]["message"][1] + f"{line_number}:{old_line}")