from progress_bar import ProgressBarHandler

import numpy as np
import math

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_animation_cheby_elastic(local_dict):
    fig = local_dict['fig']
    ax = local_dict['ax']
    line = local_dict['line']

    idisp = local_dict['idisp']
    nt = local_dict['nt']

    u_results = local_dict['u_results']

    animation_progress_handler = ProgressBarHandler(math.ceil(nt/idisp), "Creating animation...", remain_after_finish=False)

    def update(n, l):
        it = n * idisp

        l.set_ydata(u_results[n])
        
        animation_progress_handler(n)
        
        return l, 

    return animation.FuncAnimation(fig, update, math.ceil(nt/idisp), fargs=(line, ), interval=50)