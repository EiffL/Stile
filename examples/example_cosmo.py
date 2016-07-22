import sys
sys.path.append('..')
import stile
import stile.cosmo_forecasts
import numpy
def main():
    # setups
    list_of_tests = [stile.CorrelationFunctionSysTest('Rho1'),
                     stile.CorrelationFunctionSysTest('Rho2'),
                     stile.CorrelationFunctionSysTest('Rho3'),
                     stile.CorrelationFunctionSysTest('Rho4'),
                     stile.CorrelationFunctionSysTest('Rho5')]
    if True:
        data = stile.ReadTable(#'/homes/m/msimet/CFHTLenS/CFHTLens_W1_passed.fits', 
                               '/physics2/msimet/lustre/cfhtlens/CFHTLens_W1_passed.fits',
                               fields={'psf_g1': 'PSF_e1', 'psf_g2': 'PSF_e2', 'w': 'weight', 'g1': 'e1', 'g2': 'e2',
                                       'sigma': 'scalelength', 'psf_sigma': 'FLUX_RADIUS'})
        data = numpy.array(data)[:1000]
        data['sigma'] *= data['sigma']
        data['psf_sigma'] *= data['psf_sigma']
    else:
        data = numpy.rec.fromarrays((numpy.array([0.5]*10), numpy.array([0.5]*10), numpy.array([0.5]*10), numpy.array([0.5]*10), numpy.linspace(1, 10, num=10), numpy.linspace(1, 10, num=10), numpy.linspace(1, 10, num=10), numpy.linspace(1, 10, num=10), numpy.linspace(1, 10, num=10)),
                names = ['g1', 'g2', 'psf_g1', 'psf_g2', 'w', 'sigma', 'psf_sigma', 'dec', 'ra'])
    
    config = {'ra_units': 'degrees', 'dec_units': 'degrees',
                  'min_sep': 0.1, 'max_sep': 500, 'sep_units': 'arcmin', 'nbins': 25}
    list_of_results = [test(data, config=config) for test in list_of_tests]
    
    cosmo = stile.cosmo_forecasts.XiSet(data, data, config, list_of_results)
    res = cosmo.computeError()
    print res 

if __name__=='__main__':
    main()

