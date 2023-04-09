import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu


chat_id = 773978697 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.05
    p = stats.mannwhitneyu(x, y).pvalue
    return p < alpha
