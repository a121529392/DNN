import math
import random
from draw_pic import *

ID = 0



error=0
success=0
a_sort=0
b_sort=0
class Data:
    def __init__(self):
        self.in_data=[]
        self.out_data=0
    def set_input_data(self,in_data):
        self.in_data=in_data
    def set_output_data(self,out_data):
        self.out_data=out_data
class Node:
    def __init__(self, ID):
        self.cal_out = 0
        self.w = {}
        self.expect_out = 0
        self.thread = 0
        self.is_output = False
        self.ID = ID
        self.pre_node = []


    def add_pre_node(self, node):
        self.pre_node.append(node)

    def sigmoid(self):
        sum = 0
        for i in range(0, len(self.input_data), 1):
            sum += self.in_weight[i] * self.input_data[i]
        sum = 1 / (1 + math.exp(-1 * sum))
        self.cal_out = sum

    def random_weight(self):
        hold = []
        for i in range(0, len(self.input_data), 1):
            hold.append(float(random.uniform(0, 1)))
        self.weight = hold

    def set_expext_output(self, output):
        self.is_output = True
        self.expect_out = output

    def cal_thread(self):
        if self.is_output:
            self.out_thread = float(self.expect_out)
            self.thread = (self.expect_out - self.cal_out) * self.cal_out * (1 - self.cal_out)
        else:
            for i in range(0, len(self.out_weight), 1):
                self.thread.append(self.cal_out * (1 - self.cal_out) * self.out_thread * self.out_weight)

    def adjust_weight(self, rate):
        for i in range(0, len(self.in_weight), 1):
            self.in_weight[i] = self.in_weight[i] + (rate * self.thread) + self.input_data[i]

    def set_out_thread(self, out_thread):
        self.out_thread = out_thread

    def set_weight(self, weight):
        self.weight = weight

    def set_cal_out(self, cal_out):
        self.cal_out = cal_out


class Network:
    def __init__(self):
        self.node_list = []
        self.current_node = []
        self.next_node = []
        self.output_data = []
        self.input_data = []
        self.data_list=[]
        self.out_set=[]
        self.ID=0
        self.create_net_in_data = []
        self.create_net_out_data = 0
        self.accuracy = 0

    def get_node_list(self):
        return self.node_list

    def create_input_node(self):
        for i in range(0, len(self.create_net_in_data), 1):
            node = Node(self.ID)
            node.set_cal_out(self.create_net_in_data[i])
            self.ID += 1
            self.node_list.append(node)

    def create_hidden_node(self, net):
        hold = []
        for n in self.node_list:
            self.next_node.append(n)
        for i in range(0, len(net), 1):
            self.current_node = []
            for n in self.next_node:
                self.current_node.append(n)
            self.next_node = []
            for j in range(0, int(net[i]), 1):
                for n in self.current_node:
                    hold.append(n)
                node = Node(self.ID)
                self.ID += 1
                while (len(hold) > 0):
                    pre_node = hold.pop(0)
                    node.add_pre_node(pre_node.ID)
                    for x in range(0, len(self.node_list), 1):
                        if pre_node.ID == self.node_list[x].ID:
                            self.node_list[x].w[node.ID] = float(random.uniform(0, 1))
                self.node_list.append(node)
                self.next_node.append(node)

    def node_list_detail(self):
        for n in self.node_list:
            # print("I am ID : ")
            # print(n.ID)
            # print("I am cal_out : ")
            # print(n.cal_out)
            # print("I am pre_node : ")
            # print(n.pre_node)
            # print("I am weight : ")
            # print(n.w)
            # print("I am thread : ")
            # print(n.thread)
            if n.is_output:
                print("I am out_value : ")
                print(n.expect_out)
                print("I am cal_out : ")
                print (n.cal_out)

    def create_output_node(self):
        hold = []
        self.get_output_set()

        for i in range(0, len(self.output_set), 1):
            for n in self.next_node:
                hold.append(n)
            node = Node(self.ID)
            node.set_expext_output(self.output_set[i])
            self.ID += 1
            while (len(hold) > 0):
                pre_node = hold.pop(0)
                node.add_pre_node(pre_node.ID)
                for x in range(0, len(self.node_list), 1):
                    if pre_node.ID == self.node_list[x].ID:
                        self.node_list[x].w[node.ID]=float(random.uniform(0, 1))
            self.node_list.append(node)

    def cal_sigmoid(self):
        hold = []
        for x in range(0, len(self.node_list), 1):
            hold.append(self.node_list[x])
        while (len(hold) > 0):
            n = hold.pop(0)
            sum = 0
            if len(n.pre_node) > 0:
                for id in n.pre_node:
                    for j in range(0, len(self.node_list), 1):
                        if id == self.node_list[j].ID:
                            sum += self.node_list[j].w[n.ID]* self.node_list[j].cal_out
                sum = 1 / (1 + math.exp(-1 * sum))
                for i in range(0, len(self.node_list), 1):
                    if n.ID == self.node_list[i].ID:
                        self.node_list[i].cal_out = sum

    def get_all_weight(self):
        all_weight=[]
        for n in self.node_list:
            hold = []
            if len(n.w)>0:
                for key in n.w:
                    hold.append(n.w[key])
                all_weight.append(hold)

        return all_weight
    def cal_thread(self,output_data):
        hold = []
        for x in range(0, len(self.node_list), 1):
            hold.append(self.node_list[x])
        while (len(hold) > 0):
            n = hold.pop(len(hold)-1)
            if n.is_output:
                if output_data==n.expect_out:
                    n.thread= (1 - n.cal_out) * n.cal_out * (1 - n.cal_out)
                else:
                    n.thread=(0-n.cal_out)*n.cal_out*(1-n.cal_out)
            else:
                sum=0
                for next in n.w:
                    for i in range(0,len(self.node_list),1):
                        if next==self.node_list[i].ID:
                            sum+=n.w[next]*self.node_list[i].thread
                            break
                n.thread=n.cal_out*(1-n.cal_out)*sum

    def update(self,rate):
        hold = []
        for x in range(0, len(self.node_list), 1):
            hold.append(self.node_list[x])
        while (len(hold) > 0):
            n = hold.pop(len(hold) - 1)
            if len(n.w)>0:
                for next in n.w:
                    for i in range(0,len(self.node_list),1):
                        if next==self.node_list[i].ID:
                            self.node_list[n.ID].w[next]=n.w[next]+rate*self.node_list[i].thread*n.cal_out

    def train(self,train_data,train_out,rate):
        for i in range(0,len(self.node_list),1):
            if len(self.node_list[i].pre_node)==0:
                self.node_list[i].cal_out=train_data[i]
        self.cal_sigmoid()
        self.cal_thread(train_out)
        self.update(rate)
    # def get_output_value(self,in_data):


    def test(self,train_data,train_out):
        global success
        global error

        for i in range(0,len(self.node_list),1):
            if len(self.node_list[i].pre_node)==0:
                self.node_list[i].cal_out=train_data[i]
        self.cal_sigmoid()
        # print("I am expect_value : ")
        # print(train_out)
        max=0
        for i in range(0,len(self.node_list),1):
            if self.node_list[i].is_output:
                if self.node_list[i].cal_out>max:
                    max=self.node_list[i].cal_out
                    real_value=self.node_list[i].expect_out
                # print("I am out_value : ")
                # print(self.node_list[i].expect_out)
                # print("I am cal_out : ")
                # print(self.node_list[i].cal_out)

        if real_value==train_out:
            self.accuracy +=1
            success+=1
            # print("success")
        else:
            error+=1
            # print("error")
        print("i am acc")
        print(self.accuracy)
        return real_value
    def set_accuracy_value(self,acc):
        self.accuracy=acc

    def get_data(self,file):
        self.output_data=[]
        self.input_data=[]

        f=open(file,'r')
        line=f.readline()

        while line:
            line=line.split(' ')
            out=line.pop(len(line)-1)
            out=out.strip('\n')
            self.output_data.append(float(out))
            for i in range(0, len(line), 1):
                line[i] = float(line[i])
            self.input_data.append(line)
            line = f.readline()

        f.close()
    def get_output_set(self):
        self.output_set =[]
        self.output_set=list(set(self.output_data))
        for i in range(0, len(self.output_set), 1):
            self.output_set[i] = int(self.output_set[i])

    def get_create_net_data(self):

        count=random.randint(0,len(self.input_data)-1)
        self.create_net_in_data=self.input_data[count]
        self.create_net_out_data=self.output_data[count]




def get_data_list(input_data,output_data):
    data_list=[]

    for i in range(0,len(input_data),1):
        hold=Data()
        input_data[i].insert(0, -1)
        hold.set_input_data(input_data[i])
        hold.set_output_data(output_data[i])
        data_list.append(hold)

    return data_list

def run(network,rate,dir,file,train_num,accuracy):
    # draw_origin_pic()
    network = network.split(',')
    color = ['co', 'mo', 'go', 'bo', 'mo', 'yo', 'ko']
    N = Network()
    get_data_file="%s/%s.txt"%(dir,file)
    N.get_data(get_data_file)
    N.get_create_net_data()
    N.get_output_set()
    output_set_color = set_out_set_and_color(N.output_data, color)
    # print(output_set)
    data_list = get_data_list(N.input_data, N.output_data)
    # print(data_list[0].in_data)

    N.create_input_node()
    N.create_hidden_node(network)
    N.create_output_node()
    #
    N.cal_sigmoid()
    N.cal_thread(N.create_net_out_data)
    N.update(rate)
    #
    train_data_num = int(2 * len(N.input_data) / 3)
    random.shuffle(data_list)
    draw_in_x=[]
    draw_in_y=[]
    draw_out=[]
    acc_rate=0
    learing_count=0
    for i in range(0, int(train_num), 1):
        print(i)
        N.set_accuracy_value(0)

        for d in range(0, train_data_num, 1):
            N.train(data_list[d].in_data, data_list[d].out_data, rate)
        for t in range(0, len(data_list), 1):
            N.test(data_list[t].in_data, data_list[t].out_data)
        acc_rate=float(N.accuracy / len(data_list))
        if float(N.accuracy/len(data_list))>float(accuracy):
            print(float(N.accuracy/len(data_list)))
            learing_count=i
            break
    if learing_count==0:
        learing_count=train_num

    # N.node_list_detail()
    acc_train_rate=0
    N.set_accuracy_value(0)
    if train_data_num<10:
        train_data_num=0
    for d in range(train_data_num, len(data_list), 1):
        draw_out.append(N.test(data_list[d].in_data, data_list[d].out_data))
        draw_in_x.append(data_list[d].in_data[1])
        draw_in_y.append(data_list[d].in_data[2])
    acc_train_rate=float(N.accuracy/(len(data_list)-train_data_num))
    result_pic="%s_result"%file
    plot(dir,result_pic,draw_in_x,draw_in_y,draw_out,output_set_color)
    all_weight=N.get_all_weight()
    print(all_weight)
    result_data="%s/result.txt"%dir
    f = open(result_data, "w")
    f.write("data_sum:%s\n"%(len(data_list)))
    f.write("train_data_sum:%s\n" % (train_data_num))
    f.write("test_data_sum:%s\n" % (len(data_list)-train_data_num))
    f.write("acc_rate:%s\n" % (acc_rate))
    f.write("acc_train_rate:%s\n" % (acc_train_rate))
    for i in range(0,len(all_weight),1):
        f.write("w%s?%s\n" % (i,all_weight[i]))
    f.write("learning:%s\n" % (learing_count))
    f.close()
    # print("sum ")
    # print(len(data_list))
    # print("success ")
    # print(success)
    # print("error ")
    # print(error)
    # print("1: ")
    # print(a_sort)
    # print("2: ")
    # print(b_sort)
# if __name__ == "__main__":
    # network = "10"
    # rate=0.8
    # dir='C:/Users/new/Desktop/mlp_data'
    # f='2Ccircle1'
    # run(network,rate,dir,f)


