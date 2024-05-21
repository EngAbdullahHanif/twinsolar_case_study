# Metadata for PV Production and Weather Data

## Data Sources:

1. **Dpt_1_2_PV.txt**: PV production data for Department 1 and 2 buildings.
2. **ENERPOS_PV.txt**: PV production data for Enerpos building.
3. **ESIROI_PV.txt**: PV production data for ESIROI building.
4. **Meteo_Terre_Sainte.txt**: Weather data from Terre Sainte campus.

## Data Collection Methods:

- PV production data collected via installed PV systems on respective buildings.
- Weather data recorded by the Terre Sainte campus weather station.

## Preprocessing Steps:

1. Converted timestamps to a uniform format.
2. Filled missing weather data using linear interpolation.
3. Identified and corrected outliers in PV production data.
4. Normalized PV production data to ensure consistency in units.

## Columns Description:

1. **datetime**: Timestamp, end of recording period.
2. **PV Production**: PV output in kW (for respective PV data files).
3. **GHI**: Global Horizontal Irradiance in W/m2.
4. **BNI**: Beam Normal Irradiance in W/m2.
5. **DHI**: Diffuse Horizontal Irradiance in W/m2.
6. **DBT**: Dry Bulb Temperature in °C.
7. **RH**: Relative Humidity in %.
8. **Ws10**: Wind speed at 10m in m/s.
9. **Wd10**: Wind direction at 10m in degrees.
10. **Patmo**: Atmospheric pressure in mB (hPa).
11. **Rainfall**: Cumulative precipitation in mm.
