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
    print("replaced:", origin, "with:", data[line_number], sep="\n")
    return
