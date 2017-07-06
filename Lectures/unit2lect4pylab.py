import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0,30):
	mySamples.append(i)
	myLinear.append(i)
	myQuadratic.append(i**2)
	myCubic.append(i**3)
	myExponential.append(1.5**i)

#to generate plot, just call.plot(x-values, y-values)
plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

# add labels and titles
plt.figure('lin')
plt.plot(mySamples, myLinear)
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.title('Linear')
plt.figure('quad')
plt.plot(mySamples, myQuadratic)
plt.figure('cube')
plt.plot(mySamples, myCubic)
plt.figure('expo')
plt.plot(mySamples, myExponential)
# call plt.figure(<arg>), you can reopen it for processing 
plt.figure('quad')
plt.ylabel('quadratic function')
#cleaning windows cleans everything including the figure
#plt.clf()
plt.title('Quadratic')
plt.figure('cube')
plt.title('Cubic')
plt.figure('expo')
plt.title('Exponential')

# # change limits on axes 
plt.figure('lin')
plt.clf()
plt.ylim(0,1000)
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.clf()
plt.ylim(0,1000)
plt.plot(mySamples, myQuadratic)
plt.figure('lin')
plt.title('Linear')
plt.figure('quad')
plt.title('Quadratic')
 
# overylay plot and add legneds
plt.figure('lin quad')
plt.clf()
plt.ylim(0,1000)
plt.plot(mySamples, myLinear, label='linear')
plt.plot(mySamples, myQuadratic, label='quadratic')
# change the default location to upper left
plt.legend(loc='upper left')
plt.figure('cube exp')
plt.clf()
#plt.ylim(0,1000)
plt.plot(mySamples, myCubic, label='cubic')
plt.plot(mySamples, myExponential, label='exponential')
plt.legend()
plt.figure('lin quad')
plt.title('Linear vs. Quadratic')
plt.figure('cube exp')
plt.title('Cubic vs. Exponential')

plt.figure('four together')
plt.clf()
plt.ylim(0,1000)
plt.plot(mySamples, myLinear, label='linear')
plt.plot(mySamples, myQuadratic, label='quadratic')
plt.plot(mySamples, myCubic, label='cubic')
plt.plot(mySamples, myExponential, label='exponential')
plt.legend()
plt.title('Linear vs. Quadratic vs. Cubic vs. Exponential')

# color and width
# b=>blue, r=>red, g=>green, k=>black
# -=>line, o=>dot, ^=>triangle, --=>dash
plt.figure('lin quad')
plt.clf()
plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0)
plt.plot(mySamples, myQuadratic, 'ro', label='linear', linewidth=3.0)
plt.legend(loc = 'upper left')
plt.title('Linear vs. Quadratic')
plt.figure('cube exp')
plt.clf()
plt.plot(mySamples, myCubic, 'g^', label='cubic', linewidth=2.5)
plt.plot(mySamples, myExponential, 'r--', label='exponential', linewidth=3.5)
plt.legend()
plt.title('Cubic vs. Exponential')


# use subplot(compare plots side by side)
# 3 numbers => numbers of rows and cols and location
plt.figure('line quad')
plt.clf()
#the third digit 1 means top, 2 means bottom
plt.subplot(211)
plt.ylim(0,900)
plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0)
plt.title('Linear vs. Quadratic')
plt.subplot(212)
plt.ylim(0,900)
plt.plot(mySamples, myQuadratic, 'r', label='quadratic', linewidth=3.0)
plt.legend(loc = 'upper left')
plt.figure('cube exp')
plt.clf()
#the third digit 1 means left, 2 means right
plt.subplot(121)
plt.ylim(0,140000)
plt.plot(mySamples, myCubic, 'g--', label='cubic', linewidth=2.0)
plt.subplot(122)
plt.ylim(0,140000)
plt.plot(mySamples, myExponential, 'r', label='exponential', linewidth=3.0)
plt.legend()
plt.title('Cubic vs. Exponential')

plt.figure('four')
plt.clf()
#the third digit 1 means top, 2 means bottom
plt.subplot(411)
plt.ylim(0,900)
plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0)
plt.title('Linear vs. Quadratic vs.Cubic vs. Exponential')
plt.subplot(412)
plt.ylim(0,900)
plt.plot(mySamples, myQuadratic, 'r', label='quadratic', linewidth=3.0)
plt.subplot(413)
plt.ylim(0,900)
plt.plot(mySamples, myCubic, 'g--', label='cubic', linewidth=2.0)
plt.subplot(414)
plt.ylim(0,900)
plt.plot(mySamples, myExponential, 'r', label='exponential', linewidth=3.0)
plt.legend(loc = 'upper left')

# change scales
plt.figure('cube exp log')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label='cubic', linewidth=2.0)
plt.plot(mySamples, myExponential, 'r', label='exponential', linewidth=4.0)
#‘linear’ | ‘log’ | ‘logit’ | ‘symlog’
plt.yscale('log')
plt.legend()
plt.title('Cubic vs. Exponential')
plt.figure('cube exp linear')
plt.clf()
plt.plot(mySamples, myCubic, 'g--', label='Cubic', linewidth=2.0)
plt.plot(mySamples, myExponential, 'r', label='exponential', linewidth=4.0)
plt.legend()
plt.title('Cubic vs. Exponential')