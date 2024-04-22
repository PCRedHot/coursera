import matplotlib.animation as animation

def create_animation_advection_1d_euler_scheme(local_dict):
    unew_results = local_dict['unew_results']
    fig1 = local_dict['fig1']
    ax1 = local_dict['ax1']
    line1 = local_dict['line1']
    idisp = local_dict['idisp']
    nt = local_dict['nt']
    dt = local_dict['dt']
    title1 = local_dict['title1']
    
    def update(n, line):
        line.set_ydata(unew_results[n])
        ax1.set_title(title1 + ", time step: %i, time: %.2g s" % (n * idisp, n * idisp * dt))
        
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
    
    def update(n, line):
        line.set_ydata(unew_results[n])
        ax2.set_title(title2 + ", time step: %i, time: %.2g s" % (n * idisp, n * idisp * dt))
        
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
    
    def update(n, line):
        line.set_ydata(unew_results[n])
        ax3.set_title(title3 + ", time step: %i, time: %.2g s" % (n * idisp, n * idisp * dt))
        
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
    
    def update(n, line):
        line.set_ydata(unew_results[n])
        ax4.set_title(title4 + ", time step: %i, time: %.2g s" % (n * idisp, n * idisp * dt))
        
        return line,
    
    return animation.FuncAnimation(fig4, update, nt//idisp + 1, fargs=(line4, ), interval=50)