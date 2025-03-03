
# %% Script Parameters

url = 'https://uni-bonn.sciebo.de/s/oTfGigwXQ4g0raW'
filename = 'data.nc'

# %% Import Libraries
import utils
# %% Download Data
# Exercise (Example): Make a download_data(url, filename) function:

utils.download_data(url=url, filename=filename)

# %% Load Data
# Exercise: Make a `load_data(filename)` function, returning the `dset` variable.

dset = utils.load_data(filename)

# %% Extract Experiment-Level Data
# Exercise: Make an `extract_trials(filename)` function, returning the `trials` variable.


#import xarray as xr
trials = dset[['contrast_left', 'contrast_right', 'stim_onset']].to_dataframe()
trials

# %% Extract Spike-Time Data
# Exercise: Make an `extract_spikes(filename)` function, returning the `spikes` variable.


spikes = utils.extract_spikes(filename)
# %% Extract Cell-Level Data
# Exercise: Make an `extract_cells(filename)` function, returning the `cells` variable.

cells = utils.extract_cells(filename)

# %% Merge and Compress Extracted Data
# Exercise: Make a `merge_data(trials, cells, spikes)` function, returning the `merged` variable.

merged = utils.merge_data(trials, cells, spikes)


# %% Calculate Time Bins for PSTH
# Exercise: Make a `compute_time_bins(time, bin_interval)` function, returning the `time_bins` variable.
import numpy as np

time = merged['time']
time = np.round(time, decimals=6)  # Round time to the nearest microsecond, to reduce floating point errors.
bin_interval = 0.05


time_bins = utils.compute_time_bins(time, bin_interval)

# %% filter out stimuli with contrast on the right.
# No function needed here for this exercise.

filtered = merged[merged['contrast_right'] == 0]
print(f"Filtered out {len(merged) - len(filtered)} ({len(filtered) / len(merged):.2%}) of spikes in dataset.")
filtered

# %% Make PSTHs
# Exercise: Make a `compute_psths(data, time_bins)` function here, returning the `psth` variable.


psth = utils.compute_psths(filtered, time_bins, bin_interval)


# %% Plot PSTHs
# Make a `plot_psths(psth)` function here, returning the `g` variable.
import seaborn as sns


g = utils.plot_psths(psth)
g.savefig('PSTHs.png')


# %%
