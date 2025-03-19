def add_and_multiply(x, y):
    return (x + 2) * y


def compare_values(a):
    if a == 1:
        return a
    elif a > 1:
        return a - 1
    else:
        return a + 2


def boolean_operation(flag):
    return flag or False


def augment_assignment_example():
    value = 10
    value += 5
    return value


def constant_usage():
    message = 'Hello, World!'
    flag = True
    if flag:
        return message
    else:
        return 'Goodbye, World!'


def check_positive(number):
    if number <= 0:
        raise ValueError('Number must be positive.')
    return True
