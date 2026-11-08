import FreeCAD
import Import
import Mesh

doc = FreeCAD.newDocument("temp")
Import.insert("macropad-3d.step", doc.Name)

# Get all Part::Feature objects (actual geometry)
parts = []
for obj in doc.Objects:
    if obj.TypeId == "Part::Feature" and not obj.Name.startswith("Origin"):
        parts.append(obj)

print(f"Found {len(parts)} parts to export")
for p in parts:
    print(f"  - {p.Label} ({p.Name})")

# Export all parts
Mesh.export(parts, "macropad-3d-full.stl")
print("Full STL exported successfully")

# Also export just PCB + Pico for a cleaner model
pcb_pico = [p for p in parts if "PCB" in p.Label or "Pico" in p.Label or "Raspberry" in p.Label]
if pcb_pico:
    Mesh.export(pcb_pico, "macropad-pcb-pico.stl")
    print(f"PCB+Pico STL exported ({len(pcb_pico)} parts)")