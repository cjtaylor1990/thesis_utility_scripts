import numpy as np
import matplotlib.pyplot as pl
import matplotlib as mpl
import csv
import sys

default_spectrum_layout = {
    'font': {'family' : 'Times New Roman', 'weight' : 'bold', 'size'   : 22},
    'axes': {'linewidth' : 2.0},
    'xticksMajor': {'size' : 6.0, 'width' : 2.0},
    'yticksMajor': {'size' : 6.0, 'width' : 2.0},
}

def setup_spectrum_layout(spectrum_layout):
    mpl.rc('text', usetex = True)
    mpl.rc('font', **spectrum_layout['font'])
    mpl.rc('axes', **spectrum_layout['axes'])
    mpl.rc('xtick.major', **spectrum_layout['xticksMajor'])
    mpl.rc('ytick.major', **spectrum_layout['yticksMajor'])
    mpl.rc('xtick', direction = 'in')
    mpl.rc('ytick', direction = 'in')

    pl.figure(figsize=(10.,10.))

def setup_spectrum_labels(x_axis_label, y_axis_label, title=''):
    pl.xlabel(x_axis_label)
    pl.ylabel(y_axis_label)
    if title:
        pl.title(title)

def plot_spectrum(energy, value, value_label, title=''):
    setup_spectrum_layout(default_spectrum_layout)
    setup_spectrum_labels(r'$E$ (keV)', value_label, title=title)
    
    pl.xscale('log')
    pl.yscale('log')
    pl.plot(energy, value, c='k')

def save_and_clear_spectrum(outputFile):
    pl.savefig(outputFile)
    pl.clf()

def load_spectral_data(input_file, energy_index, value_index, grouped_by_column=True):
    input_data = np.load(input_file).astype('float')
    if not grouped_by_column:
        input_data = np.transpose(input_data)

    return (input_data[energy_index], input_data[value_index])

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    grouped_by_column = False if (len(sys.argv) > 3 and sys.argv[3].lower() == 'false') else True
    energy, value = load_spectral_data(input_file, 0, 2, grouped_by_column=grouped_by_column)
    
    value_label = r'$E^{2}\times$Photon Flux'
    plot_spectrum(energy, value, value_label)
    save_and_clear_spectrum(output_file)