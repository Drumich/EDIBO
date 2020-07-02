Nekas nesanāca ar event viewer logs , izdomāju ieiet kaggle un nokačāt reddit r/dataisbeautiful dataset.Vismaz kaut kas būs izdarīts.



[Add images to Github](https://youtu.be/nvPOUdz5PL4)

[Kaggle Datasets and stuff](https://www.kaggle.com/)

[Pandas API](https://pandas.pydata.org/docs/reference/index.html#api)  

[Practical Guide For Data Analysis Using Pandas](https://towardsdatascience.com/a-practical-guide-for-data-analysis-with-pandas-e24e467195a9)




``` 
import numpy as np # algebra
import pandas as pd # data processing

df = pd.read_csv(r'C:\Users\37124\Documents\Python Scripts\r_dataisbeautiful_posts.csv') # r = raw string (bez viņa nesanāca ielādēt csv)  
```   

```
df.sample(10) # show 10 random rows
```
![sample](https://user-images.githubusercontent.com/58115541/86334821-9cf09800-bc45-11ea-9934-63e0f747b391.png)

```
df.info() # Print a concise summary of a DataFrame.  
```
![info](https://user-images.githubusercontent.com/58115541/86334827-9e21c500-bc45-11ea-97b8-3971318a9c24.png)  

```
df.describe() #  Generate descriptive statistics.  
```

![desc](https://user-images.githubusercontent.com/58115541/86334826-9d892e80-bc45-11ea-9c4d-9dd47c19be33.png)   

```
df.count() # Count non-NA cells for each column or row.  
```  
![count](https://user-images.githubusercontent.com/58115541/86338263-04a8e200-bc4a-11ea-8fac-a90b83c6fb09.png)
