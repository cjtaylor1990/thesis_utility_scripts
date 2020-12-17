import matplotlib.pyplot as pl
import sys
from plot_spectrum import load_spectral_data, default_spectrum_layout, setup_spectrum_layout, save_and_clear_spectrum

def compare_spectra(test_file, control_file, saveFile='', title=''):
    test_energy, test_value = load_spectral_data(test_file, 0, 2, grouped_by_column=False)
    control_energy, control_value = load_spectral_data(control_file, 0, 1, grouped_by_column=True)

    setup_spectrum_layout(default_spectrum_layout)

    pl.plot(test_energy, test_value, c='k')
    pl.plot(control_energy, control_value, c='r')
    pl.xscale('log')
    pl.yscale('log')
    pl.ylabel(r'$E^{2}\times$Photon Flux')
    pl.xlabel(r'$E$ (keV)')
    if title:
        pl.title(title)

    if saveFile:
        save_and_clear_spectrum(saveFile)

if __name__ == "__main__":
    compare_spectra(sys.argv[1], sys.argv[2])
