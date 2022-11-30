import numpy as np
import matplotlib.pyplot as plt
#primer hist
x = np.random.uniform(0.0,5.0, 1000000)

plt.subplot(1,2,1)
plt.hist(x,100 )


#segundo hist
x = np.random.normal(5.0, 1.0, 1000000)

plt.subplot(1,2,2)
plt.hist(x, 100)
plt.suptitle("Normal Data Distribution")
plt.show()