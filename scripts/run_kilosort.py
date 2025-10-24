from spikeinterface.sorters import run_sorter

def run_kilosort(rec):
    # Run Kilosort
    """
    rec: spike interface recording object, with probe already attached!!
    """
    sorting_KS4 = run_sorter(
        sorter_name="kilosort4",
        recording=rec,
        folder="Data/Sorter_output",
        verbose=True,
    )
    return sorting_KS4