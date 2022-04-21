def parse_utf_8(str_input) -> str:
    return str(str_input, 'utf-8')


def extract_request_type(str_input) -> str:
    str_split = str_input.split("_")
    return str_split[0]


def extract_request_id(str_input) -> str:
    str_split = str_input.split("_")
    return str_split[1]