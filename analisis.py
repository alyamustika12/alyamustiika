import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Data harga dan jumlah penjualan motor
data_motor = {
    'Harga': [150000000, 170000000, 200000000, 180000000, 190000000],
    'Jumlah Penjualan': [4, 6, 5, 3, 7]
}

# Membuat DataFrame
df_motor = pd.DataFrame(data_motor)

# Menghitung koefisien korelasi Pearson antara harga dan jumlah penjualan
corr_coef, _ = pearsonr(df_motor['Harga'], df_motor['Jumlah Penjualan'])
print(f"Koefisien Korelasi antara Harga dan Jumlah Penjualan Motor: {corr_coef:.2f}")

# Membuat heatmap korelasi
plt.figure(figsize=(6, 4))
sns.heatmap(df_motor.corr(), annot=True, cmap='Pastel1', fmt=".2f")
plt.title('Heatmap Korelasi antara Harga dan Jumlah Penjualan Motor')
plt.show()
