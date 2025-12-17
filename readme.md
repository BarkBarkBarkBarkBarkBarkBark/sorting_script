


Spike Sorting & Curation — One-Page Operator Guide

Goal:
Produce a curated SpikeInterface sorting output (clean_analyzer.zarr) from raw Intan .rhd data, using AWS compute, Kilosort4, and the SpikeInterface GUI.

Final Deliverable:
A curated analyzer saved to disk (typically clean_analyzer.zarr/) and uploaded back to storage.

1. Log In & Environment Setup

Connect to the AWS instance via VS Code → Remote SSH.

Open a terminal on the remote machine.

Activate the sorting environment:

conda deactivate
conda activate sorter

2. Open & Run the Notebook

Open the Sorting Notebook in VS Code.

Set the dataset at the top of the notebook:

patient = "raw_intan"
session = "Session1"


Run cells top to bottom until one of the following exists:

A Kilosort output folder (sorted/sorter_folder/)

A SortingAnalyzer folder (sorted/analyzer_folder/)

The notebook will:

Load the Intan .rhd file

Attach the probe definition

Run Kilosort4 if needed

Build a SortingAnalyzer with waveforms, PCA, metrics, etc.

3. Launch the Spike Curation GUI

Once the analyzer exists, do not use Jupyter for curation.

From the terminal, run:

sigui --mode=web --curation "/home/marco/codespace/data/raw_intan/Session1/sorted/analyzer_folder"


Notes:

No port forwarding is required — sigui handles this automatically.

The GUI opens in your browser.

4. Perform Manual Curation (Required)

In the GUI:

Typical actions:

Mark noise units (bad waveforms, low SNR, no refractory)

Merge units that clearly belong to the same neuron

Split units if multiple waveforms are mixed

Inspect:

Waveforms

ISI histograms

PCA / feature space

Autocorrelograms

When finished:

Save in the GUI

This writes:

sorted/analyzer_folder/spikeinterface_gui/curation_data.json


That JSON file records all curation decisions.

5. Apply Curation & Save the Final Output

Return to the notebook and run the Apply Curation cell.

This step:

Applies curation_data.json to the analyzer

Writes a new curated analyzer to disk, typically:

sorted/clean_analyzer.zarr/


Important:

.zarr is a folder, not a single file

If clean_analyzer.zarr already exists, save to a new name (e.g. clean_analyzer_v2.zarr)

6. Sanity Check the Curated Sorting

The notebook will:

Load the curated analyzer

Print unit IDs and sampling frequency

Show example spike times

Confirm:

Unit count is reasonable

Units have non-empty spike trains

No deep analysis is required — this is a quick verification step.

7. Upload the Curated Result

Upload the entire clean_analyzer.zarr folder back to storage (e.g., Box).

If direct folder upload works:

box folders:upload <BOX_FOLDER_ID> "/home/marco/codespace/data/raw_intan/Session1/sorted/clean_analyzer.zarr"


If not, zip first (recommended and reliable):

cd "/home/marco/codespace/data/raw_intan/Session1/sorted"
zip -r clean_analyzer.zarr.zip clean_analyzer.zarr
box files:upload <BOX_FOLDER_ID> clean_analyzer.zarr.zip

8. What You Are Delivering

You are done when:

clean_analyzer.zarr/ exists locally

The curated output is uploaded to storage

The GUI curation JSON is preserved inside the analyzer

That folder is the final, authoritative curated result.