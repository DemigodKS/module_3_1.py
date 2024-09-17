calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    a_ = len(string)
    b_ = string.upper()
    c_ = string.lower()
    count_calls()
    return a_, b_, c_

print(string_info('Затмение'))
print(string_info('Сверхъестественное'))
print(string_info('спорт'))


def is_contains(string, list_to_search):
    count_calls()
    for word_ in list_to_search:
        if word_.casefold() in string:
            return True
    return False

print(is_contains('клубника', ['арбуз', 'банан', 'КлУбниКА']))
print(is_contains('машина', ['арбуз', 'банан', 'КлУбниКА']))

print(calls)
