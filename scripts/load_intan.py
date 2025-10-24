from spikeinterface.sorters import run_sorter
import spikeinterface.full as si
import probeinterface as pi
from pathlib import Path


def load_intan(probe):
    base_folder = Path.cwd() / "Data"
    intan_file = base_folder / "intan_data/Intan RHD 2000 file of electrophysiological recordings/Intan RHD file1.rhd"

    # Load Recording
    rec = si.read_intan(intan_file, stream_id = "0")
    rec = rec.set_probe(probe)

    n_rec = rec.get_num_channels()
    n_probe = probe.get_contact_count()

    if n_probe != n_rec:
        raise ValueError(f"Probe contacts ({n_probe}) != recording channels ({n_rec}). "
                        f"Pick the correct probe variant or subset/remap accordingly.")
    return rec