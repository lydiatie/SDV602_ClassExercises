"""
Presents an example based on Demo_Matplotlib_Browser
"""
import ChartExamples as ce 
import PySimpleGUI as sg
import matplotlib
import inspect
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close('all')

def embedded_plt(fig_dict):
    sg.theme('LightGreen')

    figure_w, figure_h = 650, 650
    # define the form layout
    listbox_values = list(fig_dict)
    col_listbox = [[sg.Listbox(values=listbox_values, enable_events=True, size=(28, len(listbox_values)), key='-LISTBOX-')],
                [sg.Text(' ' * 12), sg.Exit(size=(5, 2))]]

    layout = [[sg.Text('Matplotlib Plot Test', font=('current 18'))],
            [sg.Col(col_listbox, pad=(5, (3, 330))), sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-') ,
            sg.MLine(size=(70, 35), pad=(5, (3, 90)), key='-MULTILINE-')],]

    # create the form and show it without the plot
    window = sg.Window('Our Demo Application - Embedding Matplotlib In PySimpleGUI with **kwargs', layout, grab_anywhere=False, finalize=True)
    figure_agg = None
    # The GUI Event Loop
    while True:
        event, values = window.read()
        # print(event, values)                  # helps greatly when debugging
        if event in (sg.WIN_CLOSED, 'Exit'):             # if user closed window or clicked Exit button
            break
        if figure_agg:
            # ** IMPORTANT ** Clean up previous drawing before drawing again
            delete_figure_agg(figure_agg)
        choice = values['-LISTBOX-'][0]                 # get first listbox item chosen (returned as a list)
        func_tuple = fig_dict[choice]                         # get function to call from the dictionary
        kwargs = func_tuple[1]
        func = func_tuple[0]
        window['-MULTILINE-'].update(inspect.getsource(func))  # show source code to function in multiline
        
        fig = func(**kwargs)                                    # call function to get the figure
        figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)  # draw the figure
    window.close()

if __name__ == "__main__":
    #ce.show_figFunc(ce.bar_chart)

    # local data source

    line_plot = {'title': "Sales by Month in 2020", 
                 'xaxis': [3, 4, 4, 7, 8, 9, 14, 17, 12, 8, 8, 13], 
                 'yaxis': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                 'xlabel': 'Month',
                 'ylabel': 'Sales'}

    temperatures = {'title': "Temperature in Malaysia", 
                    'xaxis': [32, 35, 28.7, 27.2, 29.5, 26.5, 33.8, 33.1], 
                    'yaxis': list(range(1, 9)),
                    'xlabel': 'Day',
                    'ylabel': 'Temperature in Celsius'}

    min_max_temperatures = {'title': "",
                            'xaxis': [16.3, 22.1, 24.1, 18.2, 20.3, 17.0, 26.7, 24.2],
                            'xaxis1': [35.2, 34.9, 26.2, 22.4, 21.9, 25.9, 29.2, 26.5],
                            'xlabel': '',
                            'ylabel': ''}
    
    bar_chart = {'title': "Bar chart example", 
                 'xaxis': [12401, 20427, 465242, 522073, 565004, 1021987, 1460407, 2791215, 3399000, 4423016, 5403672], 
                 'xlabel': 'Years',
                 'ylabel': 'Values'}

    scatter_plot = {'title': 'This is a scatter plot',
                    'yaxis': list(np.random.randint(2, 7, (11,))), 
                    'yaxis1': list(np.random.randint(9, 14, (11,))), 
                    'yaxis2': list(np.random.randint(15, 25, (11,))), 
                    'xaxis': list(np.arange(0, 11))}  

    pie_chart = {'title': 'This is a pie chart',
                 'labels': ('C', 'Python', 'Java', 'C++', 'C#'),
                 'sizes': [13.38, 11.87, 11.74, 7.81, 4.41],
                 'explode': (0, 0.1, 0, 0, 0)}

    pie_chart1 = {'title': 'This is the second pie chart',
                 'labels': ('C', 'Python', 'Java', 'C++', 'C#', 'Others'),
                 'sizes': [13.38, 11.87, 11.74, 7.81, 4.41],
                 'explode': (0, 0.1, 0, 0, 0, 0)}


    dictionary_of_figure_functions = {'Line Plot':(ce.line_plot, line_plot),'Plot Dots(discrete plot)':(ce.discrete_plot, line_plot),
    'Name and Label':(ce.names_labels, temperatures),'Plot many Lines':(ce.multiple_plots, min_max_temperatures),
    'Bar Chart':(ce.bar_chart, bar_chart),'Histogram':(ce.histogram,{'title':'Our Histogram Name'}),
    'Scatter Plots':(ce.scatter_plots, scatter_plot),'Stack Plot':(ce.stack_plot, scatter_plot),
    'Pie Chart 1':(ce.pie_chart1, pie_chart),
    'Pie Chart 2':(ce.pie_chart2, pie_chart1)}
    
    embedded_plt(dictionary_of_figure_functions)