from matplotlib import pyplot as plt
import numpy as np

a=np.arange(0,5,0.1)
b=np.arange(0,5,0.02)

plt.subplot(221)
plt.plot(a,np.sin(a))

plt.subplot(222)
data=[9,3,2,10]
activites=['sleeping','eating','playing','working']
cols=['c','m','r','b']

plt.pie(data,
        labels=activites,
        colors=cols,
        startangle=90,
        shadow=True,
        autopct="%1.1f%%",
       explode=(0,0,0.1,0))
plt.show()

plt.subplot(223)
x=[1,2,3,4,5,6,7,8,9]
y=[5,2,4,2,1,4,5,2,5]

plt.scatter(x,y,color='r',marker='o',s=100)
plt.show()

plt.subplot(224)
plt.bar([1,3,5,7,9],[5,2,7,8,2],label='Batch1')
plt.bar([2,4,6,8,10],[8,6,2,5,6],color='g',label='Batch2')
plt.xlabel('number')
plt.ylabel('height')
plt.title('info')
plt.legend()
plt.show()
