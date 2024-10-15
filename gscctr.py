import pandas as pd
import numpy as np

df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Genio/GSC Average CTR/Queries.csv")

x = 1
y = 9
d = {'Position': [], 'Sum Clicks': [], 'Sum Impressions': [], 'Avg CTR': [], 'Min CTR': [], 'Max CTR': [], 'Max CTR KW': []}
df2 = pd.DataFrame(data=d)

while x < y:
    df1 = df[(df['Position'] >= x) & (df['Position'] < x+1)]
    df1 = df1.sort_values('CTR', ascending=False)
    df1['CTR'] = df1['CTR'].str.replace('%', '')
    df1['CTR'] = df1['CTR'].astype(np.float16)

    try:
        # Calculate values
        ctr = int(round((df1['Clicks'].sum() / df1['Impressions'].sum()) * 100))
        ctr_min = int(df1['CTR'].min())
        ctr_max = int(df1['CTR'].max())
        ctr_max_kw = df1.iloc[0]['Top queries']
        clicks = int(df1['Clicks'].sum())
        impressions = int(df1['Impressions'].sum())

        # Prepare the new row as a DataFrame
        new_row = pd.DataFrame({
            'Position': [int(x)],
            'Sum Clicks': [clicks],
            'Sum Impressions': [impressions],
            'Avg CTR': [ctr],
            'Min CTR': [ctr_min],
            'Max CTR': [ctr_max],
            'Max CTR KW': [ctr_max_kw]
        })

        # Concatenate the new row with df2
        df2 = pd.concat([df2, new_row], ignore_index=True)

    except Exception as e:
        print(f"Error processing position {x}: {e}")

    x += 1

# Convert columns to integer
df2['Avg CTR'] = df2['Avg CTR'].astype(int)
df2['Min CTR'] = df2['Min CTR'].astype(int)
df2['Max CTR'] = df2['Max CTR'].astype(int)
df2['Position'] = df2['Position'].astype(int)
df2['Sum Clicks'] = df2['Sum Clicks'].astype(int)
df2['Sum Impressions'] = df2['Sum Impressions'].astype(int)

# Convert to percentage format
df2 = df2.astype(str)
df2['Avg CTR'] = df2['Avg CTR'].apply(lambda x: x + "%")
df2['Min CTR'] = df2['Min CTR'].apply(lambda x: x + "%")
df2['Max CTR'] = df2['Max CTR'].apply(lambda x: x + "%")

df2


