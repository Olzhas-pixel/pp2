import re

def match_a_followed_by_b(string):
    return bool(re.fullmatch(r'a*b*', string))

def match_a_followed_by_two_or_three_b(string):
    return bool(re.fullmatch(r'ab{2,3}', string))

def find_lowercase_with_underscore(string):
    return re.findall(r'\b[a-z]+_[a-z]+\b', string)

def find_uppercase_followed_by_lowercase(string):
    return re.findall(r'[A-Z][a-z]+', string)

def match_a_followed_by_anything_ending_in_b(string):
    return bool(re.fullmatch(r'a.*b', string))

def replace_special_chars(string):
    return re.sub(r'[ ,.]', ':', string)

def snake_to_camel(string):
    return ''.join(word.capitalize() if i != 0 else word for i, word in enumerate(string.split('_')))

def split_at_uppercase(string):
    return re.split(r'(?=[A-Z])', string)

def insert_spaces_in_camel_case(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

def camel_to_snake(string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()

# Test cases
print(match_a_followed_by_b("abbb"))  # True
print(match_a_followed_by_two_or_three_b("abb"))  # True
print(find_lowercase_with_underscore("hello_world example_text"))  # ['hello_world', 'example_text']
print(find_uppercase_followed_by_lowercase("Hello World Python"))  # ['Hello', 'World', 'Python']
print(match_a_followed_by_anything_ending_in_b("axxxb"))  # True
print(replace_special_chars("Hello, World. Welcome"))  # 'Hello:World:Welcome'
print(snake_to_camel("this_is_a_test"))  # 'thisIsATest'
print(split_at_uppercase("HelloWorldExample"))  # ['Hello', 'World', 'Example']
print(insert_spaces_in_camel_case("HelloWorldExample"))  # 'Hello World Example'
print(camel_to_snake("HelloWorldExample"))  # 'hello_world_example'
