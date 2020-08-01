import matplotlib.pyplot as plt

loops = int(input("No Of Samples: "))
inputs = []
for x in range(loops):
    append = inputs.append(float(input()))

sum1 = 0
for num in inputs:
    sum1 += int(num)
av = sum1 / loops

ar = []
for i in range(loops - 1):
    z = 0
    z = int(inputs[i + 1]) - int(inputs[i])
    z = abs(z)
    ar.append(z)

sum = 0
for num in ar:
    sum += num

mr_bar = (sum / (loops - 1))

mr_bar

uclx = av + 2.66 * mr_bar
lclx = av - 2.66 * mr_bar

lclx

mr_bar1 = mr_bar * 3.267

mr_bar1_plot = [mr_bar1 for i in range(loops - 1)]

mr_bar_plot = [mr_bar for i in range(loops - 1)]

zero_plot = [0 for i in range(loops - 1)]

x = [i for i in range(2, loops + 1)]
x1 = [i for i in range(1, loops + 1)]

print("UCLx =", uclx)
print("CLx =", av)
print("LCLx =", lclx)
print("UCLr =", mr_bar1)
print("CLr =", mr_bar)
print("LCLr =", 0)

av_plot = [av for i in range(1, loops + 1)]
uclx_plot = [uclx for i in range(loops)]
lclx_plot = [lclx for i in range(loops)]

uclx_plot
lclx_plot

import matplotlib.pyplot as plt

f1 = plt.figure(figsize=(14, 7))
f2 = plt.figure(figsize=(14, 7))
ax1 = f1.add_subplot(111)

ax1.set_title('X Chart')
ax1.plot(x1, av_plot)
ax1.plot(x1, uclx_plot)
ax1.plot(x1, lclx_plot)

ax1.plot(x1, inputs, color='green', marker='o', linestyle='dashed')

ax2 = f2.add_subplot(111)
ax2.set_title('R Chart')
ax2.plot(x, mr_bar1_plot)
ax2.plot(x, mr_bar_plot)
ax2.plot(x, zero_plot)

ax2.plot(x, ar, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12)

plt.show()
