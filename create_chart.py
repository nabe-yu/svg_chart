import math
import os
import datetime
RECT_WH = 900  # 全体枠の縦横サイズ
CHART_R = 400  # レーダーチャート円の半径
POINT_R = 10  # ノード円の半径
SCORE_NUMBER = 5  # スコアの段階数

now = datetime.datetime.now()
score_path = f'{os.path.dirname(__file__)}\\score.txt'
template_path = f'{os.path.dirname(__file__)}\\RadarChart_template.svg'
output_path = f'{os.path.dirname(__file__)}\\output_{now:%Y%m%d-%H%M%S}.svg'

def read_score_list(score_path):
    with open(score_path, encoding='utf-8') as f:
        l = [s.strip() for s in f.readlines()]
        return l 

# ノード番号(0-15)
# スコア(1-5)

def calculate_plot_coordinate(node, score):
    node_r = CHART_R/SCORE_NUMBER * float(score)
    rad = math.pi/8 * node  # ノード数が16個なので決め打ち
    offset = RECT_WH/2 - POINT_R  # 左上が0,0なので平行移動させる
    x = round(node_r * math.cos(rad) + offset, 3)
    y = round(node_r * math.sin(rad) + offset, 3)
    return x, y 

def save_svg():
    score_list = read_score_list(score_path)
    points = []
    paths = []
    for i in range(16):
        x, y = calculate_plot_coordinate(i, score_list[i])
        if i < 15:
            next_x, next_y = calculate_plot_coordinate(i+1, score_list[i+1])
        else:
            next_x, next_y = calculate_plot_coordinate(0, score_list[0])
        point = '<circle id="Point_'+ str(i) +'" cx="10" cy="10" r="10" transform="translate('+ str(x) + ' ' + str(y) +')" fill="#707070"/>'
        points.append(point)
        path = '<path d="M ' + str(x+POINT_R) + ' ' + str(y+POINT_R) + ' ' + 'L ' + str(next_x+POINT_R) + ' ' + str(next_y+POINT_R) + '" stroke="#707070" stroke-width="3" />'
        paths.append(path)
    points_svg =  '\n'.join(points)
    paths_svg =  '\n'.join(paths)
    with open(template_path, encoding='utf-8') as f:
        s = f.read()
        result_svg = s.replace('%points%', points_svg + '\n' + paths_svg) 
    with open(output_path, 'w') as f:
        f.write(result_svg)

# Run
save_svg()