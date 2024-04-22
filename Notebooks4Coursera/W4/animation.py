from progress_bar import ProgressBarHandler

import matplotlib.pyplot as plt
import matplotlib.animation as animation


def create_animation_homogeneous(local_dict):
    fig2 = local_dict['fig2']
    ax3 = local_dict['ax3']
    up41 = local_dict['up41']
    up42 = local_dict['up42']
    
    lim = local_dict['lim']
    time = local_dict['time']
    
    idisp = local_dict['idisp']
    nt = local_dict['nt']
    
    p_results = local_dict['p_results']
    seis_results = local_dict['seis_results']

    animation_progress_handler = ProgressBarHandler(nt//idisp + 1, "Creating animation...", remain_after_finish=False)

    def update(n, up41, up42):
        it = n * idisp
        
        up41.set_ydata(seis_results[n])
        up42.set_data(time[it], seis_results[n][it])
        
        ax3.set_title('Time Step (nt) = %d' % it)
        ax3.imshow(p_results[n], vmin=-lim, vmax=+lim, interpolation="nearest", cmap=plt.cm.RdBu)

        animation_progress_handler(n)
        
        return up41, up42

    return animation.FuncAnimation(fig2, update, nt//idisp + 1, fargs=(up41, up42), interval=50)


def create_animation_advection_1d_euler_scheme(local_dict):
    unew_results = local_dict['unew_results']
    fig1 = local_dict['fig1']
    ax1 = local_dict['ax1']
    line1 = local_dict['line1']
    idisp = local_dict['idisp']
    nt = local_dict['nt']
    dt = local_dict['dt']
    title1 = local_dict['title1']

    animation_progress_handler = ProgressBarHandler(nt//idisp + 1, "Creating animation...", remain_after_finish=False)
    
    def update(n, line):
        line.set_ydata(unew_results[n])
        ax1.set_title(title1 + ", time step: %i, time: %.2g s" % (n * idisp, n * idisp * dt))

        animation_progress_handler(n)
                
        return line,
    
    return animation.FuncAnimation(fig1, update, nt//idisp + 1, fargs=(line1, ), interval=50)


def create_animation_advection_1d_predictor_corrector_scheme(local_dict):
    unew_results = local_dict['unew_results']
    fig2 = local_dict['fig2']
    ax2 = local_dict['ax2']
    line2 = local_dict['line2']
    idisp = local_dict['idisp']
    nt = local_dict['nt']
    dt = local_dict['dt']
    title2 = local_dict['title2']

    animation_progress_handler = ProgressBarHandler(nt//idisp + 1, "Creating animation...", remain_after_finish=False)

    def update(n, line):
        line.set_ydata(unew_results[n])
        ax2.set_title(title2 + ", time step: %i, time: %.2g s" % (n * idisp, n * idisp * dt))

        animation_progress_handler(n)

        return line,
    
    return animation.FuncAnimation(fig2, update, nt//idisp + 1, fargs=(line2, ), interval=50)

def create_animation_advection_1d_mccormack_scheme(local_dict):
    unew_results = local_dict['unew_results']
    fig3 = local_dict['fig3']
    ax3 = local_dict['ax3']
    line3 = local_dict['line3']
    idisp = local_dict['idisp']
    nt = local_dict['nt']
    dt = local_dict['dt']
    title3 = local_dict['title3']
    
    animation_progress_handler = ProgressBarHandler(nt//idisp + 1, "Creating animation...", remain_after_finish=False)

    def update(n, line):
        line.set_ydata(unew_results[n])
        ax3.set_title(title3 + ", time step: %i, time: %.2g s" % (n * idisp, n * idisp * dt))

        animation_progress_handler(n)
        
        return line,
    
    return animation.FuncAnimation(fig3, update, nt//idisp + 1, fargs=(line3, ), interval=50)

def create_animation_advection_1d_lax_wendroff_scheme(local_dict):
    unew_results = local_dict['unew_results']
    fig4 = local_dict['fig4']
    ax4 = local_dict['ax4']
    line4 = local_dict['line4']
    idisp = local_dict['idisp']
    nt = local_dict['nt']
    dt = local_dict['dt']
    title4 = local_dict['title4']
    
    animation_progress_handler = ProgressBarHandler(nt//idisp + 1, "Creating animation...", remain_after_finish=False)

    def update(n, line):
        line.set_ydata(unew_results[n])
        ax4.set_title(title4 + ", time step: %i, time: %.2g s" % (n * idisp, n * idisp * dt))

        animation_progress_handler(n)
        
        return line,
    
    return animation.FuncAnimation(fig4, update, nt//idisp + 1, fargs=(line4, ), interval=50)