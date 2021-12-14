import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
pd.options.mode.chained_assignment = None

%%time
data = pd.read_excel('sensors.py')