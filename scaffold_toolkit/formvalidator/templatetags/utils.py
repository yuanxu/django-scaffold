from django.utils import translation


def convert_datetime_python_to_javascript(input_format):
    input_format = input_format.replace('%Y', 'YYYY')
    input_format = input_format.replace('%m', 'MM')
    input_format = input_format.replace('%d', 'DD')
    input_format = input_format.replace('%H', 'h')
    input_format = input_format.replace('%M', 'm')
    input_format = input_format.replace('%S', 's')
    return input_format


def get_language():
    parts = translation.get_language().splite('-')
    parts[1] = parts[1].upper()
    return '_'.join(parts)