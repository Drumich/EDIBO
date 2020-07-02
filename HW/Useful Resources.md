[Kaggle Datasets and stuff](https://www.kaggle.com/)

[Pandas API](https://pandas.pydata.org/docs/reference/index.html#api)  

[Practical Guide For Data Analysis Using Pandas](https://towardsdatascience.com/a-practical-guide-for-data-analysis-with-pandas-e24e467195a9)























This might not be the most efficient way to convert nested json records in a text file (delimited by line) to DataFrame object, but it kinda does the job.
 ```import pandas as pd
import json
from pandas.io.json import json_normalize

with open('path_to_your_text_file.txt', 'rb') as f:
    data = f.readlines()

data = map(lambda x: eval(json_normalize(json.loads(x.rstrip())).to_json(orient="records")[1:-1]), data)
e = pd.DataFrame(data)
print e.head()```
