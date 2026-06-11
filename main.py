import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Generate simulated kinetic data for protein induction expression levels
np.random.seed(42)
time_hours = np.linspace(0, 8, 9)

# Simulated target protein yields (mg/L) based on standard BL21 culture kinetics
control_uninduced = 0.5 * time_hours + np.random.normal(0, 0.1, len(time_hours))
induced_bl21 = 12.0 / (1 + np.exp(-(time_hours - 3))) + np.random.normal(0, 0.2, len(time_hours))

# Create a clean pandas DataFrame
data_dict = {
    'Time_Hours': time_hours,
    'Control_Uninduced_mgL': np.clip(control_uninduced, 0, None),
    'Induced_BL21_mgL': np.clip(induced_bl21, 0, None)
}
df = pd.DataFrame(data_dict)

print("--- Recombinant Protein Expression Pipeline Analytics ---")
print(df.to_string(index=False))

# 2. Generate a publication-quality data visualization
plt.figure(figsize=(8, 5))
plt.plot(df['Time_Hours'], df['Induced_BL21_mgL'], marker='o', color='#2ca02c', linewidth=2.5, label='Induced E. coli BL21')
plt.plot(df['Time_Hours'], df['Control_Uninduced_mgL'], marker='s', color='#7f7f7f', linewidth=1.5, linestyle='--', label='Uninduced Control')

# Style plot to match standard biological publication formatting
plt.title('Recombinant Protein Expression Kinetics Post-IPTG Induction', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Time Post-Induction (Hours)', fontsize=10)
plt.ylabel('Target Protein Concentration (mg/L)', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper left', frameon=True)
plt.xlim(0, 8)
plt.ylim(0, 14)

# Save output data visual as a static asset
plt.tight_layout()
plt.savefig('protein_expression_curve.png', dpi=300)
print("\n[Success] Analysis executed. Plot saved as 'protein_expression_curve.png'")
