# Load the Pandas libraries with alias 'pd' 
import pandas as pd
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("~/1502421.csv", sep=",", verbose=True, nrows=5)
# Preview the first 5 lines of the loaded data 
data = data.drop(['MonthlyTotalSeasonToDateCoolingDD', 'MonthlyTotalSeasonToDateHeatingDD', 'MonthlyDeptFromNormalCoolingDD'], axis=1)
data = data.drop(['MonthlyTotalCoolingDegreeDays', 'MonthlyDeptFromNormalHeatingDD'], axis=1)
data = data.drop(['MonthlyMinSeaLevelPressureTime', 'MonthlyTotalHeatingDegreeDays'], axis=1)
data = data.drop(['MonthlyMinSeaLevelPressureValue', 'MonthlyMinSeaLevelPressureDate'], axis=1)
data = data.drop(['MonthlyDaysWithGT90Temp', 'MonthlyDaysWithLT32Temp', 'MonthlyDaysWithGT32Temp'], axis=1)
data = data.drop(['MonthlyDaysWithLT0Temp', 'MonthlyDaysWithGT001Precip'], axis=1)
data = data.drop(['MonthlyDaysWithGT010Precip', 'MonthlyDaysWithGT1Snow'], axis=1)
data = data.drop(['MonthlyMaxSeaLevelPressureValue', 'MonthlyMaxSeaLevelPressureDate'], axis=1)
data = data.drop(['MonthlyMaxSeaLevelPressureTime'], axis=1)
data = data.drop(['MonthlyDeptFromNormalMinimumTemp', 'MonthlyDeptFromNormalAverageTemp'], axis=1)
data = data.drop(['MonthlyDeptFromNormalPrecip', 'MonthlyTotalLiquidPrecip'], axis=1)
data = data.drop(['MonthlyGreatestPrecip', 'MonthlyGreatestPrecipDate', 'MonthlyGreatestSnowfall'], axis=1)
data = data.drop(['MonthlyGreatestSnowfallDate', 'MonthlyGreatestSnowDepth', 'MonthlyGreatestSnowDepthDate'], axis=1)
data = data.drop(['MonthlyAverageRH', 'MonthlyDewpointTemp', 'MonthlyDeptFromNormalMaximumTemp'], axis=1)
data = data.drop(['MonthlyWetBulbTemp', 'MonthlyAvgHeatingDegreeDays'], axis=1)
data = data.drop(['MonthlyAvgCoolingDegreeDays', 'MonthlyStationPressure'], axis=1)
data = data.drop(['MonthlySeaLevelPressure', 'MonthlyAverageWindSpeed', 'MonthlyTotalSnowfall'], axis=1)
data = data.drop(['MonthlyMaximumTemp', 'MonthlyMinimumTemp', 'MonthlyMeanTemp'], axis=1)
data = data.drop(['DAILYPrecip', 'DAILYSnowfall', 'DAILYSnowDepth', 'DAILYAverageStationPressure'], axis=1)
data = data.drop(['DAILYAverageSeaLevelPressure', 'DAILYAverageWindSpeed', 'DAILYPeakWindSpeed'], axis=1)
data = data.drop(['PeakWindDirection', 'DAILYSustainedWindSpeed', 'DAILYSustainedWindDirection'], axis=1)

data = data.drop(['DAILYAverageDryBulbTemp', 'DAILYDeptFromNormalAverageTemp', 'DAILYAverageRelativeHumidity'], axis=1)
data = data.drop(['DAILYAverageDewPointTemp', 'DAILYAverageWetBulbTemp', 'DAILYHeatingDegreeDays', 'DAILYCoolingDegreeDays'], axis=1)
data = data.drop(['DAILYMinimumDryBulbTemp', 'DAILYWeather'], axis=1)

#print(data.head())

#print(list(data.columns.values))

print(data.to_csv(index_label='idx'))

