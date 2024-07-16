import time
from functools import wraps

def delay(seconds):
    def decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapped_function
    return decorator

@delay(5)
def it_may_be(name=''):
    return (name + "ask: It's nearly Luncheon Time?\n")

# Вінні-Пух запитує: "Вже майже час обіду?"
for t in range(12):
    print(it_may_be(name='Winnie-the-Pooh'))
