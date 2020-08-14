import pandas as pd

data = pd.read_table('hits.txt', names=('host', 'ip', 'page'))
print(*data['ip'].value_counts().index[:5], sep='\n')

# answer
# 154.157.157.156
# 82.146.232.163
# 194.78.107.33
# 226.247.119.128
# 21.143.243.182
