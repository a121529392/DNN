import matplotlib
from ipykernel.pylab.backend_inline import FigureCanvas
matplotlib.use('Qt5Agg')
import numpy as np
import matplotlib.pyplot as plt
import os
data_dir="./mlp_data"
class draw_pic:
    def __init__(self):
        self.data_dir="./mlp_data"
        self.input_x=[]
        self.input_y=[]
        self.out_data = []
        self.file = []
        self.color=['co','mo','go','bo','yo','ko']

    def set_dir(self,dir):
        self.data_dir=dir

    def get_file_list(self):
        data_list = os.listdir(self.data_dir)
        data_file = []
        for f in data_list:
            data_file.append("%s/%s" % (self.data_dir, f))
            if ".txt" in f:
                if "result" not in f:
                    f = f.replace('.txt', '')
                    self.file.append(f)


    def get_data(self,file):
        self.input_x = []
        self.input_y = []
        self.out_data = []
        f = open(file, 'r')
        line = f.readline()

        while line:
            line = line.split(' ')
            out = line.pop(len(line) - 1)
            out = out.strip('\n')
            self.out_data.append(int(out))

            for i in range(0, len(line), 1):
                if i == 0:
                    self.input_x.append(float(line[i]))
                else:
                    self.input_y.append(float(line[i]))

            line = f.readline()

        f.close()


def plot(dir,f,input_x,input_y,out_data,out_color):


    plt.cla()

    fig = plt.figure(figsize=(3, 3))
    cavans = FigureCanvas(fig)
    max_x = max(input_x) + 1
    min_x = min(input_x) - 1
    max_y = max(input_y) + 1
    min_y = min(input_y) - 1

    # ax =self.fig.add_axes([0.1,0.5,0.2,0.2])
    ax = fig.add_subplot(111)
    # self.axes.set_position([0.2, 0.2, 0.6, 0.6])
    ax.set_xlim([min_x, max_x])
    ax.set_ylim([min_y, max_y])
    print(input_x)
    print(input_y)
    for i in range(0, len(input_x), 1):
        for c in out_color:
            if out_data[i] == c:
                ax.plot(input_x[i], input_y[i], out_color[c])
    # ironman = np.linspace(-1, 1, 1000)
    # ironman2 = np.linspace(-1, 1, 1000)
    # y = ironman ** 2*ironman2
    # ax.plot(ironman, y, '.', color='SteelBlue', label='Sine')
    cavans.draw()
    # ax.legend()
    # plt.show()
    pic = "%s/%s.png" % (dir, f)
    fig.savefig(pic)



def set_out_set_and_color(out_data,color):
    output_set = list(set(out_data))
    out_color={}
    for o in output_set:

        out_color[round(o)]=color[round(o)]
    return out_color

def draw_origin_pic():
    draw = draw_pic()
    draw.get_file_list()
    for f in draw.file:
        file = "%s/%s.txt" % (draw.data_dir, f)
        draw.get_data(file)
        out_color=set_out_set_and_color(draw.out_data,draw.color)
        print(out_color)
        plot(draw.data_dir,f,draw.input_x,draw.input_y,draw.out_data,out_color)


if __name__ == '__main__':
    draw_origin_pic()


    # print(file)
    # for f in file:
    #     plot(f)