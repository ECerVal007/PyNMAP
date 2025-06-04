#!/usr/bin/env python
# -*- coding: utf -8 -*-
__author__ = "Edgar Cervantes"
__email__ = "Evalencia2@students.columbiabasin.edu"
__date__ = "Spring 2025"
__version__ = "0.0.1"

from pathlib import Path
from datetime import date
import subprocess
import json
import pickle

# Get the directory where the script is running
script_path = Path(__file__).resolve().parent

# Define "Logon ID" folder path
logon_id_dir = script_path / "Logon ID"

# Check if the folder exists, and create it if not
if not logon_id_dir.exists():
    logon_id_dir.mkdir()
    print(f"Info: Created 'Logon ID' directory at: {logon_id_dir}")
else:
    print(f"Info: 'Logon ID' directory already exists at: {logon_id_dir}")

today_stamp = date.today().strftime("%m%d%y")

#define your target network
network = "192.168.1.0/24"

nmap_cmd = ["nmap", "-T4", "-sS", "-n","-oX", "-", network]
print(f'Running Nmap on {network}...')

result = subprocess.run(nmap_cmd, capture_output=True, text=True)
nmap_output = result.stdout

# Save XML
xml_path = logon_id_dir / f"{today_stamp}.xml"
with open(xml_path, "w", encoding="utf-8") as xf:
    xf.write(nmap_output)
print(f"Saved XML: {xml_path}")

# Save JSON
json_path = logon_id_dir / f"{today_stamp}.json"
with open (json_path, "w") as jf:
    json.dump({"nmap_output": nmap_output}, jf, indent=2)
print(f"Saved JSON: {json_path}")

# Save Pickle
pickle_path = logon_id_dir / f"{today_stamp}.pickle"
with open(pickle_path, 'wb')as pf:
    pickle.dump(nmap_output,pf)
print(f'Saved Pickle: {pickle_path}')