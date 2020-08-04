from tkinter import *
from tkinter import ttk
import os
from Node import *
from draw_pic import *
data_dir="./mlp_data"
file=[]
result_data=[]
def get_file_list():
    global file
    file = []
    data_list = os.listdir(data_dir)
    data_file = []
    for f in data_list:
        data_file.append("%s/%s" % (data_dir, f))
        if ".txt" in f :
            if "result" not in f:
                f = f.replace('.txt', '')
                file.append(f)
    print(file)
get_file_list()

def get_result_data():
    global result_data
    result_data = []
    result="%s/result.txt"%data_dir
    f = open(result, 'r')
    line = f.readlines()
    for l in line:
        l=l.strip('\n')
        if ':' in l:
            hold=l.split(':')[1]
            result_data.append(hold)
        else:
            hold = l
            result_data.append(hold)
        # print(hold)
    f.close()
    print(result_data)


class Testi():
    def __init__(self):
        self.canvas = Canvas(root, width = 500, height = 480)

        self.img = PhotoImage(file="%s/%s.png"%(data_dir,file[0]))
        self.imgArea = self.canvas.create_image(0, 0, anchor = NW, image = self.img)
        self.canvas.place(x=450, y=40, anchor='nw')
        self.but1 = Button(root, text=" OK ", command=lambda: self.changeImg())
        self.but1.place(x=10, y=300)
        self.labelTop = Label(root, text="choose data set", font=('Arial', 14))
        self.labelTop.place(x=10, y=5)
        self.labelTop = Label(root, text="data picture", font=('Arial', 14))
        self.labelTop.place(x=550, y=5)

        self.combo_file = ttk.Combobox(root,
                                    values=file, font=('Arial', 12))
        self.combo_file.place(x=10, y=40)
        self.combo_file.current(0)

        Label(root, text='learning rate :', font=('Arial', 14)).place(x=10, y=80)
        Label(root, text='Convergence condition (accuracy):', font=('Arial', 14)).place(x=10, y=110)
        Label(root, text='network:', font=('Arial', 14)).place(x=10, y=170)
        Label(root, text='training count:', font=('Arial', 14)).place(x=10, y=200)
        Label(root, text='data num:', font=('Arial', 14)).place(x=10, y=330)
        Label(root, text='training data num:', font=('Arial', 14)).place(x=10, y=360)
        Label(root, text='testing data num:', font=('Arial', 14)).place(x=10, y=390)
        Label(root, text='training accuracy rate:', font=('Arial', 14)).place(x=10, y=420)
        Label(root, text='testing accuracy rate:', font=('Arial', 14)).place(x=10, y=450)
        Label(root, text='learning count:', font=('Arial', 14)).place(x=10, y=490)
        Label(root, text='weight:', font=('Arial', 14)).place(x=10, y=530)

        self.lr_setting = StringVar()
        self.lr_setting.set('0.8')
        self.entry_lr_setting = Entry(root, textvariable=self.lr_setting, font=('Arial', 14))
        self.entry_lr_setting.place(x=130, y=80)

        self.end_condition = StringVar()
        self.end_condition.set('0.99')
        self.end_condition = Entry(root, textvariable=self.end_condition, font=('Arial', 14))
        self.end_condition.place(x=10, y=140)

        self.network_layer = StringVar()
        self.network_layer.set('5,4')
        self.network_layer = Entry(root, textvariable=self.network_layer, font=('Arial', 14))
        self.network_layer.place(x=100, y=170)

        self.train_num = StringVar()
        self.train_num.set('500')
        self.train_num = Entry(root, textvariable=self.train_num, font=('Arial', 14))
        self.train_num.place(x=10, y=230)

        self.data_sum_var = StringVar()
        self.data_sum_var.set('0')
        self.data_sum = Label(root, textvariable=self.data_sum_var, font=('Arial', 14))
        self.data_sum.place(x=100, y=330)

        self.train_data_sum_var = StringVar()
        self.train_data_sum_var.set('0')
        self.train_data_sum = Label(root, textvariable=self.train_data_sum_var, font=('Arial', 14))
        self.train_data_sum.place(x=170, y=360)

        self.test_data_sum_var = StringVar()
        self.test_data_sum_var.set('0')
        self.test_data_sum = Label(root, textvariable=self.test_data_sum_var, font=('Arial', 14))
        self.test_data_sum.place(x=170, y=390)

        self.acc_rate_var = StringVar()
        self.acc_rate_var.set('0')
        self.acc_rate = Label(root, textvariable=self.acc_rate_var, font=('Arial', 14))
        self.acc_rate.place(x=220, y=420)

        self.acc_rate_test_var = StringVar()
        self.acc_rate_test_var.set('0')
        self.acc_rate_test = Label(root, textvariable=self.acc_rate_test_var, font=('Arial', 14))
        self.acc_rate_test.place(x=220, y=450)

        self.lear_num_var = StringVar()
        self.lear_num_var.set('0')
        self.lear_num = Label(root, textvariable=self.lear_num_var, font=('Arial', 14))
        self.lear_num.place(x=220, y=490)

        self.weight = StringVar()
        self.weight.set('0')
        self.weight = Label(root, textvariable=self.weight, font=('Arial', 14))
        self.weight.place(x=120, y=530)

        self.count_weight = 0
        self.count=0
    def changeImg(self):
        self.img = PhotoImage(file="%s/%s.png"%(data_dir,self.combo_file.get()))
        self.canvas.itemconfig(self.imgArea, image = self.img)
        print (self.end_condition.get())
        run(self.network_layer.get(), float(self.lr_setting.get()), data_dir, self.combo_file.get(),int(self.train_num.get()),self.end_condition.get())
        if self.count==0:

            self.canvas_res = Canvas(root, width=500, height=480)
            self.img_res = PhotoImage(file="%s/%s_result.png" % (data_dir,self.combo_file.get()))
            self.imgArea_res = self.canvas_res.create_image(0, 0, anchor=NW, image=self.img_res)
            self.canvas_res.place(x=450, y=450, anchor='nw')
        else:
            self.img_res = PhotoImage(file="%s/%s_result.png" % (data_dir,self.combo_file.get()))
            self.canvas_res.itemconfig(self.imgArea, image=self.img_res)
        get_result_data()
        learn_count = result_data[len(result_data) - 1]
        print("i am learn")
        print(learn_count)
        self.data_sum.pack()
        self.data_sum.destroy()
        self.data_sum_var = StringVar()
        self.data_sum_var.set(result_data[0])
        self.data_sum = Label(root, textvariable=self.data_sum_var, font=('Arial', 14))
        self.data_sum.place(x=100, y=330)

        self.train_data_sum.pack()
        self.train_data_sum.destroy()
        self.train_data_sum_var = StringVar()
        self.train_data_sum_var.set(result_data[1])
        self.train_data_sum = Label(root, textvariable=self.train_data_sum_var, font=('Arial', 14))
        self.train_data_sum.place(x=170, y=360)

        self.test_data_sum.pack()
        self.test_data_sum.destroy()
        self.test_data_sum_var = StringVar()
        self.test_data_sum_var.set(result_data[2])
        self.test_data_sum = Label(root, textvariable=self.test_data_sum_var, font=('Arial', 14))
        self.test_data_sum.place(x=170, y=390)

        self.acc_rate.pack()
        self.acc_rate.destroy()
        self.acc_rate_var = StringVar()
        self.acc_rate_var.set(result_data[3])
        self.acc_rate = Label(root, textvariable=self.acc_rate_var, font=('Arial', 14))
        self.acc_rate.place(x=220, y=420)

        self.acc_rate_test.pack()
        self.acc_rate_test.destroy()
        self.acc_rate_test_var = StringVar()
        self.acc_rate_test_var.set(result_data[4])
        self.acc_rate_test = Label(root, textvariable=self.acc_rate_test_var, font=('Arial', 14))
        self.acc_rate_test.place(x=220, y=450)

        self.lear_num.pack()
        self.lear_num.destroy()
        self.lear_num_var = StringVar()
        self.lear_num_var.set(learn_count)
        self.lear_num = Label(root, textvariable=self.lear_num_var, font=('Arial', 14))
        self.lear_num.place(x=220, y=490)
        w=[]
        print(result_data)
        learn_count=result_data[len(result_data)-1]
        print("i am learn")
        print(learn_count)
        for i in range(5,len(result_data)-1,1):
            w.append(result_data[i].split('?')[0])
        self.comboExample = ttk.Combobox(root,
                                         values=w, font=('Arial', 12))
        self.comboExample.place(x=120, y=530)
        self.comboExample.current(0)
        self.comboExample.bind("<<ComboboxSelected>>", self.display_weight)
        # self.weight = StringVar()
        # self.weight.set('0')
        # self.weight = Label(root, textvariable=self.weight, font=('Arial', 14))
        # self.weight.place(x=10, y=540)

    def display_weight(self,event):

        pos=self.comboExample.get()
        Label(root, text='%s:'%self.comboExample.get(), font=('Arial', 14)).place(x=10, y=550)
        Label(root, text='%s:' % self.comboExample.get(), font=('Arial', 14)).place(x=10, y=550)
        for i in range(0,len(result_data)-1,1):
            if str(i) in pos:
                if self.count_weight!=0:
                    self.weight.pack()
                    self.weight.destroy()
                self.count_weight+=1
                self.weight_var = StringVar()
                self.weight_var.set(result_data[5+i].split('?')[1])
                self.weight = Label(root,wraplength=500, textvariable=self.weight_var, font=('Arial', 14))
                self.weight.place(x=10, y=580)
                # Label(root,wraplength=500,text=result_data[5+i].split('?')[1], font=('Arial', 14),justify=LEFT).place(x=10, y=540)


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x800")
    print(file)
    app = Testi()
    root.mainloop()