import matplotlib.pyplot as plot 
import math
MARKER = "."
MARKER_SIZE = 7
LINE_WIDTH = 2
FONT_SIZE = 10
N_ROWS = 2
N_COLUMNS = 3
(figures, axes) = plot.subplots(N_ROWS, N_COLUMNS)


def graph_settings(graph_type, x_array, y_array, color):
    graph_type.plot(x_array, y_array, marker = MARKER, ms = MARKER_SIZE, lw = LINE_WIDTH, color = color)
    graph_type.set_xticks(x_array)
    graph_type.grid(axis = "x")
    graph_type.grid(axis = "y")
    graph_type.set_xlabel("X-Axis", fontsize = 8)
    graph_type.set_ylabel("Y-Axis", fontsize = 8)

def make_graphs(ax, title, x_array, function, color):
    graph_y = []

    for element in x_array:
        graph_y.append(function(element))

    graph_settings(ax, x_array, graph_y, color)
    ax.set_title(title)

#plot 1: linear
#plot 2: quadratic
#plot 3: cubic
#plot 4: logarithmic
#plot 5: exponential
make_graphs(axes[0,0], "Linear Graph", [1,2,3,4,5], lambda x: x, "blue")
make_graphs(axes[0,1], "Quadratic Graph", [-3,-2,-1,0,1,2,3], lambda x: x**2,  "red")
make_graphs(axes[0,2],  "Cubic Graph", [1,2,3,4,5], lambda x: x**3, "orange")
make_graphs(axes[1,0], "Logarithmic Graph", [1,2,3,4,5], math.log, "green")
make_graphs(axes[1,1], "Exponential Graph", [1,2,3,4,5], lambda x: 2**x, "purple")

#plot 6: last 6 years of Union College's population
union = axes[1,2]
union.set_title("Union's Population")
union_x = ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
union_y = [2189, 2047, 2096, 2107, 2082, 2065]
union.plot(union_x,union_y)
union.set_ylim(bottom = 2000, top = 2200)
union.grid(axis = "x")
union.grid(axis = "y")
union.set_xlabel("Year", fontsize = 10, color = "black")
union.set_ylabel("Population", fontsize = 10, color = "black")
union.tick_params(axis = "x", labelsize = "4")


plot.tight_layout()
plot.show()
