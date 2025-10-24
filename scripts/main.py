import download_intan_data
import create_custom_probe
import load_intan
import run_kilosort
import create_sorting_analyzer
import run_curation_gui

def main():
    download_intan_data.download_intan_data()
    probe = create_custom_probe.create_custom_probe()
    rec = load_intan.load_intan(probe)
    sorter = run_kilosort.run_kilosort(rec)
    create_sorting_analyzer.create_sorting_analyzer(probe, sorter)
    run_kilosort.run_kilosort(rec)

if __name__ == '__main__':
    main()

    
