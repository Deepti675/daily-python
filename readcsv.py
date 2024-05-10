from google.colab import drive
drive.mount('/content/drive')
import pandas as pd

file_path = '/content/drive/My Drive/path/to/your/file.csv'
df = pd.read_csv(file_path)
