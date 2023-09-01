import sys

import api.variables as var
from api.interpreter import *
from api.console import *
from api.open import *

console = Console()
file_path = open_file()

if not file_path:
    console.error(language_dictionary[var.language]["errors"][2])
    console.info(language_dictionary[var.language]["exit_code"][0] + "-2" + language_dictionary[var.language]["exit_code"][1])
    console.show()
    sys.exit()

file = open(file_path, "r", encoding="utf-8")

for line in file:
    var.old_line = line
    try:
        process(line)
    except Exception as e:
        console.error(language_dictionary[var.language]["errors"][0] + f"{line_number}|'{old_line}'")
        console.error(language_dictionary[var.language]["errors"][1] + f"{e.args}")
        console.info(language_dictionary[var.language]["exit_code"][0] + "-1" + language_dictionary[var.language]["exit_code"][1])
        console.show()
        sys.exit()
    line_number += 1

console.info(language_dictionary[var.language]["exit_code"][0] + "0" + language_dictionary[var.language]["exit_code"][1])
console.show()