def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    with open(file_name, "r") as read_obj:
        for line in read_obj:
            if string_to_search in line:
                list_of_results.append((line_number, line.rstrip()))
            line_number += 1
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results


def replace_line_with(file_name, line_number, new_line):
    with open(file_name, "r", encoding="utf-8") as file:
        data = file.readlines()
    origin = str(data[line_number])
    data[line_number] = new_line

    with open(file_name, "w", encoding="utf-8") as file:
        file.writelines(data)

        line1 = (
            f"{colors.reset}{'replaced: ' : ^11}"
            + f"{colors.fg.lightred}--- {origin.strip() : ^10}{colors.reset}"
        )
        line2 = (
            f"{'with: ' : ^11}"
            + f"{colors.fg.lightgreen}+++"
            f" {data[line_number].strip() : ^10}{colors.reset}"
        )
        line3 = (
            f"in {colors.fg.lightcyan}{file_name}{colors.reset} at line {line_number}"
        )
        print(line1, line2, line3, sep="\n")

    return


class colors:
    """Colors class:reset all colors with colors.reset; two
    sub classes fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold"""

    reset = "\033[0m"
    bold = "\033[01m"
    disable = "\033[02m"
    underline = "\033[04m"
    reverse = "\033[07m"
    strikethrough = "\033[09m"
    invisible = "\033[08m"

    class fg:
        black = "\033[30m"
        red = "\033[31m"
        green = "\033[32m"
        orange = "\033[33m"
        blue = "\033[34m"
        purple = "\033[35m"
        cyan = "\033[36m"
        lightgrey = "\033[37m"
        darkgrey = "\033[90m"
        lightred = "\033[91m"
        lightgreen = "\033[92m"
        yellow = "\033[93m"
        lightblue = "\033[94m"
        pink = "\033[95m"
        lightcyan = "\033[96m"

    class bg:
        black = "\033[40m"
        red = "\033[41m"
        green = "\033[42m"
        orange = "\033[43m"
        blue = "\033[44m"
        purple = "\033[45m"
        cyan = "\033[46m"
        lightgrey = "\033[47m"


# print(colors.bg.green, "SKk", colors.fg.red, "Amartya")
# print(colors.bg.lightgrey, "SKk", colors.fg.red, "Amartya")
