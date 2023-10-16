AllPrices = []
CurrentPrice = 0
import random
import time
start_value = 15
a_list = []

def runcode():
    def number_Multipla(start_value,a_list):

        #while True:
        for i in range (10) :
            #Numbers Going Up
            HighProbUp = [1,1.01,1.02,1.03,1.04,1.05,1.06,1.07,1.08,1.09,1.1,1.11,1.12,1.13,1.14,1.15,1.16,1.17,1.18,1.19]
            MedProbUp = [1.2,1.21,1.22,1.23,1.24,1.25,1.26,1.27,1.28,1.29,1.3,1.31,1.32,1.33,1.34,1.35,1.36,1.37,1.38,1.39]
            LowProbUp  = [1.4,1.41,1.42,1.43,1.44,1.45,1.46,1.47,1.48,1.49,1.5,1.51,1.52,1.53,1.54,1.55,1.56,1.57,1.58,1.59,1.6]
            VeryLowProbUp = [1.6,1.61,1.62,1.63,1.64,1.65,1.66,1.67,1.68,1.69,1.7,1.71,1.72,1.73,1.74,1.75,1.76,1.77,1.78,1.79,1.8,1.81,1.82,1.83,1.84,1.85,1.86,1.87,1.88,1.89,1.9,1.91,1.92,1.93,1.94,1.95,1.96,1.97,1.98,1.99]

            # Code for prices going up
            a = random.choice(HighProbUp)
            b = random.choice(MedProbUp)
            c = random.choice(LowProbUp)
            d = random.choice(VeryLowProbUp)
            UpList = [a,b,c,d]

            PrecentUp = random.choices(UpList, weights = (100,20,5,1), k=1)

            # Numbers Going Down
            HighProbDown = [0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99,1]
            MedProbDown = [0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79]
            LowProbDown  = [0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59]
            VeryLowProbDown = [0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39]
            # Code for prices going down
            aa = random.choice(HighProbDown)
            bb = random.choice(MedProbDown)
            cc = random.choice(LowProbDown)
            dd = random.choice(VeryLowProbDown)
            UpList = [aa,bb,cc,dd]

            PrecentDown = random.choices(UpList, weights = (100,20,5,1), k=1)

            # Code for displayed price
            this_list = [PrecentDown,PrecentUp]
            out_value = random.choice(this_list)
            out_value = str(out_value)
            res = str(out_value)[1:-1]
            return res




    import random
    from itertools import count
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    plt.style.use('ggplot')

    x_vals = []
    y_vals = []

    index = count()


    def animate(i):
        num = float(number_Multipla(start_value, a_list))
        nums = num * 15
        x_vals.append(next(index))
        y_vals.append(nums)
        plt.cla()
        plt.plot(x_vals, y_vals)

    ani = FuncAnimation(plt.gcf(), animate,interval=1500)
    plt.tight_layout()
    plt.show()

        # data = pd.read_csv('data.csv')
        # x = data['x_value']
        # y1 = data['total_1']
        # y2 = data['total_2']
    #
    #
    #
    # #print(number_Multipla())
    # f = open("Data.txt","w+")
    # for i in range(10):
    #     f.write(number_Multipla(start_value,a_list))
    #     f.write('\r')
    #     time.sleep(5)
