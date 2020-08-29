import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16])
plt.show()
#Default is blue line 

plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.axis([0,6,0,20])
plt.show()

#Displayed red dot line,axis : x (0,6) y(0,20) 

import numpy as np
t = np.arange(0.,5.,0.2)
print(t)
t1 = np.arange(0,5,0.5)
t1
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()
plt.plot(t1,t1,'r--',t1,t1**2,'bs',t1,t1**3,'g^')
plt.show()
#Displayed red dash line, blue square , green triangle 
# 


data = { 'a': np.arange(50),
        'c':np.random.randint(0,50,50),
        'd':np.random.randn(50) }
plt.plot(data['a'],data['c'],'g^',data['a'],data['d'],'r--')
plt.show()
# Displays  two graphs in gree triangle and red dash 

data['b'] = data['a'] + 10* np.random.randn(50)
data['d'] = np.abs(data['d']) *100
plt.scatter('a','b','c','d',data=data)
plt.show()
# Displays  scatter circles of very small size

plt.scatter('a','b',c='c',s='d',data=data)
plt.show()
# Displays  scatter circles of random size

names = ['sahasra','sasi','dinesh']
values=[2,31,36]
plt.figure(figsize=(9,3))
#plt.subplot(1)  subplot should be in 3 digits

plt.subplot(111)
plt.subplot(222)
plt.subplot(333)
plt.bar(names,values)
plt.scatter(names,values)
plt.plot(names,values)
plt.suptitle('Categorical Plotting')
plt.show()
# Displays in right top corner as subplot areas are 111/222

plt.subplot(131)
plt.subplot(132)
plt.subplot(133)
plt.show()
# Displays three empty subplot areas 

plt.subplot(131)
plt.subplot(132)
plt.subplot(133)
plt.bar(names,values)
plt.scatter(names,values)
plt.plot(names,values)
plt.suptitle('Categorical Plotting')
plt.show()
# Displays twp  empty subplot areas and has bar/scatter/line in the last subplot

plt.subplot(131)
plt.bar(names,values)
plt.subplot(132)
plt.scatter(names,values)
plt.subplot(133)
plt.plot(names,values)
plt.suptitle('Categorical Plotting')
plt.show()
# Displays  bar/scatter/line in subplots respectively 

mu,sigma = 100,15
x= mu+ sigma*np.random.randn(10000)
plt.hist(x,50,density=1,facecolor='g',alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.axis([40, 160, 0, 0.03])
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.grid(True)
plt.show()

# Displays Histogram with text annotate on particular axis with scientific symbol notation


t=nplt.arrange(0.0,5.0,0.01)
t=np.arrange(0.0,5.0,0.01)
t=np.arange(0.0,5.0,0.01)
s=np.cos(2*np.pi*t)
plt.plot(t,s,lw=2)
plt.show()
# Displays cos wave with y graph limited max and min of y values which is 1,-1

plt.plot(t,s,lw=2)
plt.ylim(-2,2)
plt.show()
# Displays cos wave with y graph set to 2,-2


plt.plot(t,s,lw=2)
plt.annotate('local max',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='red',shrink=0.05))
plt.ylim(-2,2)
plt.show()
# Displays cos wave with y graph set to 2,-2 and annotate text at 2,1 of the graph and mouse hover will display the values
