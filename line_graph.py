from dot_plot import * 
from bar_chart import *
from pie_chart import *
def line_graph(frejm):
    print('Wykres liniowy')
    for widget in frejm.winfo_children():
        widget.destroy()
    
    