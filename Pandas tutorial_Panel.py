import numpy as np
import pandas as pd

data1=np.random.rand(2,4,5)
d1=pd.Panel(data1)
print(d1)
