import subprocess
from pathlib import Path

RAW_ROOT_BOX_FOLDER_ID = "352606395707"
BASE_FOLDER = Path.home() / "codespace" / "data"

def run_box(args):
    proc = subprocess.run(["box", *args], capture_output=True, text=True, check=True)
    return proc.stdout

def get_child_folder_id(parent_id: str, child_name: str) -> str:
    out = run_box(["folders:items", parent_id, "--csv", "--fields", "type,id,name"])
    # parse CSV manually
    lines = out.strip().splitlines()
    header = lines[0].split(",")
    rows = [dict(zip(header, l.split(","))) for l in lines[1:]]
    matches = [r for r in rows if r.get("type") == "folder" and r.get("name") == child_name]
    if len(matches) != 1:
        raise RuntimeError(f"Expected exactly one '{child_name}' under {parent_id}, found {matches}")
    return matches[0]["id"]

def download_patient(patient_name: str) -> Path:
    pid = get_child_folder_id(RAW_ROOT_BOX_FOLDER_ID, patient_name)
    subprocess.run(["box", "folders:download", pid, "--destination", str(BASE_FOLDER), "--create-path", "--yes"], check=True)
    return BASE_FOLDER / patient_name

def upload_all_sorted(patient_name: str) -> None:
    pid = get_child_folder_id(RAW_ROOT_BOX_FOLDER_ID, patient_name)
    local_patient = BASE_FOLDER / patient_name
    for session in local_patient.iterdir():
        sorted_dir = session / "sorted"
        if not sorted_dir.is_dir():
            continue
        sid = get_child_folder_id(pid, session.name)
        subprocess.run(["box", "folders:upload", str(sorted_dir), "--parent-folder", sid, "--yes"], check=True)
