Pweave Example - Frequency response of a moving average filter
==============================================================

:Author: Matti Pastell <matti.pastell@helsinki.fi>
:Website: http://mpastell.com

**Create 11 point moving average filter and plot its frequency response and print the values.**

::

  from pylab import *
  import scipy.signal as signal
  #A function to plot frequency and phase response
  def mfreqz(b,a=1):
      w,h = signal.freqz(b,a)
      h = abs(h)
      return(w/max(w), h)


 
**Make the impulse response function and format the code chunk and output as doctest block.**


>>> n = 11.
>>> n
11.0
>>> b = repeat(1/n, n)
>>> print(b)
[ 0.09090909  0.09090909  0.09090909  0.09090909  0.09090909  0.09090909
  0.09090909  0.09090909  0.09090909  0.09090909  0.09090909]


 

**Calculate the frequency response and plot it:**

::

  w, h = mfreqz(b)
  #Plot the function
  plot(w,h,'k')
  ylabel('Amplitude')
  xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
  show()


.. figure:: images/Fig1.*
   :width: 15 cm

   Frequency response of an 11 point moving average filter

 

**The first 10 values of the frequency response (w,h) as a table, notice that the code is hidden in the output document.**

.. csv-table::
   :header: "Amplitude", "Frequency"


   1.0 , 0.0
   1.0 , 0.0
   1.0 , 0.0
   1.0 , 0.01
   1.0 , 0.01
   1.0 , 0.01
   0.99 , 0.01
   0.99 , 0.01
   0.99 , 0.02
   0.98 , 0.02

