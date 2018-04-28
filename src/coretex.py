import types
from celery import Celery
import skills
from stimulus import Stimulus

app = Celery('coretex',
             backend='rpc://guest@localhost//',
             broker='pyamqp://guest@localhost//')


def decorate_all_in_module(module, decorator):
    for name in dir(module):
        obj = getattr(module, name)
        if isinstance(obj, types.FunctionType):
            setattr(module, name, decorator(obj))


decorate_all_in_module(skills, app.task)

# the brain part

type = input('Type.\n')
text = input('Master, what is my purpose?\n')

s = Stimulus(type, text=text)

if s.type == 'command':
    print(skills.pass_the_butter())
