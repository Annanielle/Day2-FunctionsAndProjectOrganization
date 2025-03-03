
# %% Script Parameters

url = 'https://uni-bonn.sciebo.de/s/oTfGigwXQ4g0raW'
filename = 'data.nc'

# %% Import Libraries
import src.ptsh.utils as utils
# %% Download Data
utils.download_data(url=url, filename=filename)

# %% Load Data
dset = utils.load_data(filename)

# %% Extract Experiment-Level Data
trials = dset[['contrast_left', 'contrast_right', 'stim_onset']].to_dataframe()
trials

# %% Extract Spike-Time Data
spikes = utils.extract_spikes(filename)

# %% Extract Cell-Level Data
cells = utils.extract_cells(filename)

# %% Merge and Compress Extracted Data
merged = utils.merge_data(trials, cells, spikes)

# %% Calculate Time Bins for PSTH
time = merged['time']
time = np.round(time, decimals=6)  # Round time to the nearest microsecond, to reduce floating point errors.
bin_interval = 0.05

time_bins = utils.compute_time_bins(time, bin_interval)

# %% filter out stimuli with contrast on the right.
filtered = merged[merged['contrast_right'] == 0]
print(f"Filtered out {len(merged) - len(filtered)} ({len(filtered) / len(merged):.2%}) of spikes in dataset.")

# %% Make PSTHs
psth = utils.compute_psths(filtered, time_bins, bin_interval)

# %% Plot PSTHs
g = utils.plot_psths(psth)
g.savefig('PSTHs.png')

# %%
