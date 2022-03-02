import netCDF4    
from netCDF4 import Dataset,chartostring
import numpy as np
try: ncfile.close()
except: pass 

predictor_out = netCDF4.stringtochar(np.array(['constant'], 'S8'))
channels_out = [4]
ncfile = Dataset('VIIRS_bias.nc',mode='w',format='NETCDF4') 
print(ncfile)

ncfile.title = 'VIIRS Bias predictors'
ncfile._ioda_layout = 'ObsGroup'
ncfile._ioda_layout_version = 0
print(ncfile.title)
print(ncfile._ioda_layout)

coef_dim = ncfile.createDimension('bias_coefficients', 1) 
coef_err_dim = ncfile.createDimension('bias_coeff_errors', 1) 
npredictors = ncfile.createDimension('npredictors',1) 
nchannels = ncfile.createDimension('nchannels',1)
#predictors_dim = ncfile.createDimension('predictors', 1) 
coef = ncfile.createVariable('bias_coefficients', np.float, ('bias_coefficients',))
coef_error = ncfile.createVariable('bias_coeff_errors', np.float, ('bias_coeff_errors',)) 
predictors = ncfile.createVariable('predictors', 'S8', ('npredictors',)) 
channels = ncfile.createVariable('channels', np.int, ('nchannels',))
coef.units = 'Aerosol optical depth'
coef.long_name = 'bias_coefficients' 
coef_error.units = 'Aerosol optical depth'
coef_error.long_name = 'bias_coeff_errors' 
print(coef) 


n_coef = len(coef_dim)
coef[:] = -0.0163 
coef_error[:] = .0863  
predictor2 = netCDF4.chartostring(predictor_out)   
print(predictor2) 
predictors[:] = predictor2 
channels[:] = channels_out 
print(coef)
print(coef_error)

print(ncfile) 
ncfile.close() 
