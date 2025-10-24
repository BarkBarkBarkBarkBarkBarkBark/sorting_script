import spikeinterface.full as si
from spikeinterface_gui import run_mainwindow

def run_curation_gui():
    sorting_analyzer = si.load_sorting_analyzer(folder="Data/intan_analyzer")

    run_mainwindow(sorting_analyzer, mode="web", curation=True)

def main():
    run_curation_gui()



if __name__ == "__main__":
    main()
