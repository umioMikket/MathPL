variables = {}
user_functions = {}

old_line = ""
line_number = 1

language = "eng"
language_dictionary = {
    "eng": {
        "message": {
            0: "Message '",
            1: "' from '"
        },
        "errors": {
            0: "An unknown error occurred: ",
            1: "More details: ",
            2: "The file opening window was closed or rejected!",
            3: {
                0: "Incorrect number of arguments for the function '",
                1: "' in "
            },
            4: "The expression is written incorrectly: ",
            5: "It is impossible to divide by zero in the expression: ",
            6: "The time limit for the execution of the expression is overcome: ",
            7: "There was a memory leak in the expression: ",
            8: "Incorrect arithmetic expression: ",
            9: {
                0: "You entered the wrong language in the function: ",
                1: "Available: eng, ru"
            }
        },
        "lang_info": {
            0: "MathPl",
            1: "a language demonstrating my Python programming skills",
            2: "Author: umioMikket (GitHub) - Konovalov Mihail"
        },
        "exit_code": {
            0: "Exit with code: ",
            1: ", see details in docs/exit_codes.txt",
        }
    },
    "ru": {
        "message": {
            0: "Сообщение '",
            1: "' от '"
        },
        "errors": {
            0: "Произошла неизвестная ошибка: ",
            1: "Подробнее: ",
            2: "Окно открытия файла был закрыт или отклонен!",
            3: {
                0: "Неверное количество аргументов для функции '",
                1: "' в "
            },
            4: "Неверно написанно выражение: ",
            5: "Делить на ноль нельзя в выражении: ",
            6: "Преодален придел времени по выполнению выражения: ",
            7: "Произошла утечка памяти в выражении: ",
            8: "Неверное арефметическое выражение: ",
            9: {
                0: "Вы ввели неверный язык в функцию: ",
                1: "Доступные: eng, ru"
            }
        },
        "lang_info": {
            0: "MathPl",
            1: "язык демонстрирующий мои навыки программирования на Python.",
            2: "Автор: umioMikket (GitHub) - Коновалов Михаил"
        },
        "exit_code": {
            0: "Выход с кодом: ",
            1: ", смотрите подробнее в docs/exit_codes.txt",
        }
    }
}