from pathlib import Path
import requests, zipfile, io
import os

def download_intan_data():
    """
    The data is intracranial mouse recording, from a 16 channel microarray. 
    The paper can be found here: https://doi.org/10.1371/journal.pone.0221510
    """

    url = "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/w767nnk5wh-1.zip"
    base_folder = Path.cwd() / "Data"
    zip_path = base_folder / "intan_data.zip"
    extract_to = base_folder / "intan_data"

    if os.path.exists(extract_to):
        print("file exists!")
    else:

        print("Downloading File...")
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(zip_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Download complete: {zip_path}")

        # 3. Unzip to a folder
        print("Extracting files...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

        print(f"Files extracted to: {extract_to}")