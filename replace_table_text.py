import math
import os
import datetime

now = datetime.datetime.now()
text_path = f'{os.path.dirname(__file__)}\\text.txt'
template_path = f'{os.path.dirname(__file__)}\\table_template.svg'
output_path = f'{os.path.dirname(__file__)}\\output_{now:%Y%m%d-%H%M%S}.svg'


def read_text_list(text_path):
    with open(text_path, encoding='utf-8') as f:
        l = [s.strip() for s in f.readlines()]
        return l


def save_svg():
    text_list = read_text_list(text_path)
    with open(template_path, encoding='utf-8') as f:
        s = f.read()
        for i in range(5):
            s = s.replace(f'%text_{i}%', text_list[i])
    with open(output_path, 'w' , encoding='utf-8') as f:
        f.write(s)


# Run
save_svg()
