import spikeinterface.full as si
from pathlib import Path
import os

def create_sorting_analyzer(probe, sorter):
    """
    Probe: spike interface probe object
    Sorter: 
    """

    base_folder = Path.cwd() / "Data"
    intan_file = base_folder / "intan_data/Intan RHD 2000 file of electrophysiological recordings/Intan RHD file1.rhd"
    sa_path = base_folder / "intan_analyzer"
    if os.path.exists(""):

    # Load Recording
    recording = si.read_intan(intan_file, stream_id = "0")
    recording = recording.set_probe(probe, in_place=False)
    recording = si.unsigned_to_signed(recording)
    recording_filtered = si.bandpass_filter(recording)

    job_kwargs = dict(n_jobs=-1, progress_bar=True, chunk_duration="1s")

    sorting_analyzer = si.create_sorting_analyzer(sorter, recording_filtered, overwrite = True,
    format="binary_folder", folder=sa_path,
    **job_kwargs )
    sorting_analyzer.compute("random_spikes", method="uniform", max_spikes_per_unit=500)
    sorting_analyzer.compute("waveforms", **job_kwargs)
    sorting_analyzer.compute("templates", **job_kwargs)
    sorting_analyzer.compute("noise_levels")
    sorting_analyzer.compute("unit_locations", method = "monopolar_triangulation")
    sorting_analyzer.compute("isi_histograms")
    sorting_analyzer.compute("correlograms", window_ms=100, bin_ms=5)
    sorting_analyzer.compute("principal_components", n_components=3, mode="by_channel_global", whiten=True, **job_kwargs)
    sorting_analyzer.compute("quality_metrics", metric_names=["snr", "firing_rate"])
    sorting_analyzer.compute("template_similarity")
    sorting_analyzer.compute("spike_amplitudes", **job_kwargs)