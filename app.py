import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import warnings
warnings.filterwarnings('ignore')

# Cài đặt font hiển thị tiếng Việt tốt hơn
plt.rcParams.update({
    'figure.dpi': 120,
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 11,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# ── Đọc dữ liệu ──
df_raw = pd.read_csv('giaxang.csv')
df_raw.columns = ['Ngay', 'RON95', 'E5RON92', 'DO', 'KO']
df_raw['Ngay'] = pd.to_datetime(df_raw['Ngay'], dayfirst=True)

# ── Lọc 2021–2025 ──
df = df_raw[df_raw['Ngay'].dt.year.between(2021, 2025)].copy()
df = df.reset_index(drop=True)

# ── Đổi đơn vị: ×1000 để ra VNĐ/lít ──
for col in ['RON95', 'E5RON92', 'DO', 'KO']:
    df[col] = (df[col] * 1000).round(0).astype(int)

# ── Thêm cột phụ trợ ──
df['Nam']   = df['Ngay'].dt.year
df['Thang'] = df['Ngay'].dt.month
df['Thang_Nam'] = df['Ngay'].dt.to_period('M')

print(f"Tổng số kỳ điều chỉnh (2021–2025): {len(df)}")
print(f"Phạm vi: {df['Ngay'].min().date()} → {df['Ngay'].max().date()}")
print()
df[['Ngay','RON95','E5RON92','DO','KO']].head(10)
