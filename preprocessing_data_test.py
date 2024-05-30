import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dpt_1_2_pv = pd.read_csv("TwInSolar_consolidated_data-main/Dpt_1_2_PV.txt", delimiter=",")
enerpos_pv = pd.read_csv("TwInSolar_consolidated_data-main/ENERPOS_PV.txt", delimiter=",")
esiroi_pv = pd.read_csv("TwInSolar_consolidated_data-main/ESIROI_PV.txt", delimiter=",")
meteo = pd.read_csv("TwInSolar_consolidated_data-main/Meteo_Terre_Sainte.txt", delimiter=",")


# print(dpt_1_2_pv.head())
# print("-------------------")
# print(dpt_1_2_pv.describe())
# print("-------------------")

# columns names 
# print(dpt_1_2_pv.columns)
# print(enerpos_pv.columns)
# print(esiroi_pv.columns)
# print(meteo.columns)


# check if timestamp is in datatime format
# print(dpt_1_2_pv['datetime'].head())
# print(enerpos_pv['datetime'].head())
# print(esiroi_pv['datetime'].head())
# print(meteo['datetime'].head())


# check if there are missing values 
# print("Dpt_1_2_PV: ", dpt_1_2_pv.isnull().sum())
# print("ENERPOS_PV: ", enerpos_pv.isnull().sum())
# print("ESIROI_PV: ", esiroi_pv.isnull().sum())
# print("Meteo_Terre_Sainte: ", meteo.isnull().sum())

# checking for outliers, visually ploting to inspect the outliers
# sns.boxplot(data=dpt_1_2_pv[['Prod_kW']])
# plt.title('Boxplot for Dpt_1_2 PV Production')
# plt.show()

# sns.boxplot(data=enerpos_pv[['Prod_kW']])
# plt.title('Boxplot for Enerpos PV Production')
# plt.show()

# sns.boxplot(data=esiroi_pv[['Prod_kW']])
# plt.title('Boxplot for ESIROI PV Production')
# plt.show()



# Statistical method to identify outliers
# dpt_1_2_pv_outliers = dpt_1_2_pv[(dpt_1_2_pv['Prod_kW'] < (dpt_1_2_pv['Prod_kW'].mean() - 3 * dpt_1_2_pv['Prod_kW'].std())) | (dpt_1_2_pv['Prod_kW'] > (dpt_1_2_pv['Prod_kW'].mean() + 3 * dpt_1_2_pv['Prod_kW'].std()))]
# print("Outliers in Dpt_1_2 PV Production:", len(dpt_1_2_pv_outliers))

# enerpos_pv_outliers = enerpos_pv[(enerpos_pv['Prod_kW'] < (enerpos_pv['Prod_kW'].mean() - 3 * enerpos_pv['Prod_kW'].std())) | (enerpos_pv['Prod_kW'] > (enerpos_pv['Prod_kW'].mean() + 3 * enerpos_pv['Prod_kW'].std()))]
# print("Outliers in Enerpos PV Production:", len(enerpos_pv_outliers))

# esiroi_pv_outliers = esiroi_pv[(esiroi_pv['Prod_kW'] < (esiroi_pv['Prod_kW'].mean() - 3 * esiroi_pv['Prod_kW'].std())) | (esiroi_pv['Prod_kW'] > (esiroi_pv['Prod_kW'].mean() + 3 * esiroi_pv['Prod_kW'].std()))]
# print("Outliers in ESIROI PV Production:", len(esiroi_pv_outliers))