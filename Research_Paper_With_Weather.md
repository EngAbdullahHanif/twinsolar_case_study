### Paper 1: Location Agnostic Adaptive Rain Precipitation Prediction using Deep Learning

**Target Variable:**
- Rain precipitation (mm)

**Features:**
- Meteorological Data: Average air temperature at 2 meters (T2M), Dew point at 2 meters (T2MDEW), Wet point at 2 meters (T2MWET), Earth Skin Temperature (TS), Merra-2 Temperature at 2 meters range (T2M RANGE), Maximum temperature at 2 meters (T2M MAX), Minimum temperature at 2 meters (T2M MIN), Specific Humidity at 2 meters (QV2M), Relative Humidity at 2 meters (RH2M), Bias-corrected total precipitation at 2 meters (PRECTOT), Average surface pressure at surface (PS), Average wind speed 10 meters range (WS10M RANGE), Average wind speed 10 meters high (WS10M), Average wind direction 10 meters high (WD10M), Maximum wind speed 10 meters (WS10M MAX), Minimum wind speed 10 meters (WS10M MIN)

**Models:**

| Model                     | Mean Square Error |
|---------------------------|-------------------|
| Adaboost                  | 96.7630           |
| Gradient Boosting Regressor | 102.7857        |
| Random Forest Regressor   | 85.8252           |
| Stacking Regressor        | 112.3288          |
| Deep Neural Network       | 79.8080           |

**City-wise Performance:**

| City        | Before Adaptation MAE | After Adaptation MAE |
|-------------|-----------------------|----------------------|
| Paris       | 69.0626 %             | 25.8855 %            |
| Los Angeles | 11.3367 %             | 6.3358 %             |
| Tokyo       | 56.2065 %             | 17.5864 %            |

**Limitations:**
- The model heavily depends on the accuracy and availability of weather data, which can vary significantly across different regions.
- The complexity of implementing domain adaptation techniques adds to the computational burden, making real-time applications challenging.
- While the model shows significant improvements for the specific target locations tested (Paris, Los Angeles, and Tokyo), its ability to generalize to entirely new, unseen locations was not extensively tested or proven.

---

### Paper 2: A Two-Step Approach to Solar Power Generation Prediction Based on Weather Data Using Machine Learning

**Target Variable:**
- Solar power generation

**Features:**
- Weather Forecast Data: Rainfall Type, Sky Type, Wind Direction, Wind Speed, Humidity, Temperature, Solar Elevation
- Weather Observation Data: Radiation, Vapor Pressure, Surface Temperature, Atmospheric Pressure
- Derived Variables: Week Number, Time Zone

**Models:**

| Model      | Base Model RMSE | Base Model R² | Main Model RMSE | Main Model R² | Improvement RMSE | Improvement R² |
|------------|-----------------|---------------|-----------------|---------------|------------------|----------------|
| Adaboost   | 669.5           | 0.604         | 609.2           | 0.672         | 60.3 (9.0%)      | 0.068          |
| Linear Reg | 635.5           | 0.643         | 608.6           | 0.673         | 26.9 (4.2%)      | 0.030          |
| CART       | 619.2           | 0.661         | 607.9           | 0.673         | 11.3 (-1.8%)     | 0.012          |
| SVR        | 689.9           | 0.579         | 605.7           | 0.676         | 84.2 (12.2%)     | 0.097          |
| ANN        | 606.0           | 0.675         | 597.4           | 0.684         | -8.6 (1.4%)      | 0.009          |
| k-NN       | 630.2           | 0.649         | 596.4           | 0.686         | -35.8 (5.7%)     | 0.037          |
| RFR        | 581.5           | 0.701         | 596.4           | 0.705         | 4.0 (-0.7%)      | 0.004          |

**Limitations:**
- It heavily depends on the accuracy of weather forecasts, which can be uncertain.
- The generation of auxiliary variables adds complexity and potential inaccuracies.
- Computational demands are high, making real-time applications challenging.
- The model's performance may not generalize well to different locations or long-term climate variations.

---


### Paper 3: Prediction model of household appliance energy consumption

**Target Variable:**
- Energy consumption of household appliances (Wh)

**Features:**
- Temperature (T1-T9)
- Humidity (R1-R9)
- Light energy consumption (L)
- Humidity outside the airport (RO)
- Dew point temperature (Td)
- Visibility (V)
- Wind speed (W)
- Temperature outside the airport (TO)
- Random Variables (rv1, rv2)
- Pressure (P)

**Models:**

| Model | Training R² | Training RMSE | Testing R² | Testing RMSE |
|-------|-------------|---------------|------------|--------------|
| KNN   | 0.86        | 37.08         | 0.58       | 64.99        |
| SVM   | 0.83        | 41.13         | 0.57       | 65.52        |
| RF    | 0.94        | 23.84         | 0.57       | 65.64        |
| ERF   | 0.99        | 9.99          | 0.64       | 59.81        |
| LSTM  | 0.97        | 2.48          | 0.97       | 21.36        |

**Limitations:**
- The research is limited by its data specificity to a single house in Belgium, which restricts generalizability to other regions.
- Feature selection may have overlooked important non-linear relationships.
- Traditional machine learning models showed signs of overfitting, indicating possible complexity issues.
- The lack of external validation raises concerns about model robustness, and the computational complexity of the LSTM model poses challenges for real-time applications.
