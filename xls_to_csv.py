import pandas as pd
import openpyxl
df = pd.read_excel('python_test.xlsx')
df.to_csv('output_test.csv', index=False)




