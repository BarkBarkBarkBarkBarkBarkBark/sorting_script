# Create custom probe geometry if needed
import probeinterface as pi

probe = pi.Probe(ndim=2)
positions = []

for i in range(16):
    positions.append([0, i * 50])
probe.set_contacts(positions = positions, shapes = "circle", shape_params = {'radius':5})

probe.set_device_channel_indices(range(16))
probe.set_contact_ids([f"ch{i}" for i in range(16)])

probe_path =  "~/codespace/sorting_script/Custom_Probes/neuronexus-A16x1_2mm_50_177_A16.json"
pi.write_probeinterface(probe_path, probe)