import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu


chat_id = 773978697 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.1
    p_y = y_success / y_cnt
    p_x = x_success / x_cnt
    p = (y_success + x_success) / (y_cnt + x_cnt)
    std = np.sqrt(p * (1 - p) / y_cnt + p * (1 - p) / x_cnt)
    z = (p_y - p_x) / std
    z_crit = norm.ppf(1 - alpha)
    answer = True if z > z_crit else False
    return answer
