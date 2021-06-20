# dataframe_to_image
Python package to convert a Pandas DataFrame to a Image that could be used to share dataframe (as an image) in sheets, notes and slides.


Example usage:

```python
import pandas as pd
from dataframe_to_image import dataframe_to_image
#creating the dataframe
df = pd.DataFrame()
df['date'] = ['2021-06-01', '2021-06-02', '2021-06-03']
df['calories'] = [1950, 2100, 1500]
df['sleep hours'] = [9, 7.5, 8.2]
df['gym'] = [True, False, False]
#converting to image
dataframe_to_image.convert(df,visualisation_library='matplotlib')
```
![Example Output](../main/images/example.png)
