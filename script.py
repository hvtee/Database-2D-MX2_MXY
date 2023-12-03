import os
import re
import sqlite3

# structure
compound = None
crystal_system = None
lattice_constants = None
lattice_angles = None
layer_thickness = None
international = None
space_group = None
symmetry_operations = None

# bands
band_gap = None
eigenvalue_vbm = None
eigenvalue_cbm = None
fermi_energy = None
highest_occupied_band = None
lowest_unoccupied_band = None
loc_vbm_up = None
loc_cbm_up = None
loc_vbm_dw = None
loc_cbm_dw = None
loc_vbm_to = None
loc_cbm_to = None

# cell

lattice_vectors = None
ion_positions = None

# energy_mag_mom
total_energy = None
total_magnetization = None

# mechanical
stiffness_tensor = None
youngs_modulus = None
shear_modulus = None
poisson_ratio = None
bulk_modulus = None
shear_modulus_mechanical = None
bulk_shear_ratio = None

# wf
vacuum_level = None
work_function = None


def process_structure_file(filepath):
    global compound, crystal_system, lattice_constants, lattice_angles, layer_thickness
    global international, space_group, symmetry_operations

    with open(filepath, 'r') as file:
        content = file.read()
        print(file.name)

        compound = re.search(r'Compound:\s*([\w-]+)', content).group(1)
        crystal_system = re.search(r'2D Crystal System:\s*([\w\s]+)', content).group(1)
        lattice_constants = re.search(r'Lattice Constants:\s*([\d.\s]+)', content).group(1)
        lattice_angles = re.search(r'Lattice Angles:\s*([\d.\s]+)', content).group(1)
        layer_thickness = float(re.search(r'Layer Thickness:\s*([\d.-]+)', content).group(1))
        international = re.search(r'International:\s*([\S-]+)', content).group(1)
        space_group = float(re.search(r'Space Group:\s*(\d+)', content).group(1))
        symmetry_operations = float(re.search(r'Symmetry Operations:\s*(\d+)', content).group(1))


def process_bands_file(filepath):
    global band_gap, eigenvalue_vbm, eigenvalue_cbm, fermi_energy
    global highest_occupied_band, lowest_unoccupied_band
    global loc_vbm_up, loc_cbm_up, loc_vbm_dw, loc_cbm_dw, loc_vbm_to, loc_cbm_to

    with open(filepath, 'r') as file:
        content = file.read()
        print(file.name)

        band_gap_match = re.search(r'Band Gap \(eV\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        eigenvalue_vbm_match = re.search(r'Eigenvalue of VBM \(eV\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        eigenvalue_cbm_match = re.search(r'Eigenvalue of CBM \(eV\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        fermi_energy_match = re.search(r'Fermi Energy \(eV\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        highest_occupied_band_match = re.search(r'Highest-Occupied Band:\s*(\d+)\s*(\d+)\s*(\d+)', content)
        lowest_unoccupied_band_match = re.search(r'Lowest-Unoccupied Band:\s*(\d+)\s*(\d+)\s*(\d+)', content)
        loc_vbm_up_match = re.search(r'Location of VBM \(UP\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        loc_cbm_up_match = re.search(r'Location of CBM \(UP\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        loc_vbm_dw_match = re.search(r'Location of VBM \(DW\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        loc_cbm_dw_match = re.search(r'Location of CBM \(DW\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        loc_vbm_to_match = re.search(r'Location of VBM \(TO\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        loc_cbm_to_match = re.search(r'Location of CBM \(TO\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)

        band_gap = f"{band_gap_match.group(1)} {band_gap_match.group(2)} {band_gap_match.group(3)}"
        eigenvalue_vbm = f"{eigenvalue_vbm_match.group(1)} {eigenvalue_vbm_match.group(2)} {eigenvalue_vbm_match.group(3)}"
        eigenvalue_cbm = f"{eigenvalue_cbm_match.group(1)} {eigenvalue_cbm_match.group(2)} {eigenvalue_cbm_match.group(3)}"
        fermi_energy = f"{fermi_energy_match.group(1)} {fermi_energy_match.group(2)} {fermi_energy_match.group(3)}"
        highest_occupied_band = f"{highest_occupied_band_match.group(1)} {highest_occupied_band_match.group(2)} {highest_occupied_band_match.group(3)}"
        lowest_unoccupied_band = f"{lowest_unoccupied_band_match.group(1)} {lowest_unoccupied_band_match.group(2)} {lowest_unoccupied_band_match.group(3)}"
        loc_vbm_up = f"{loc_vbm_up_match.group(1)} {loc_vbm_up_match.group(2)} {loc_vbm_up_match.group(3)}"
        loc_cbm_up = f"{loc_cbm_up_match.group(1)} {loc_cbm_up_match.group(2)} {loc_cbm_up_match.group(3)}"
        loc_vbm_dw = f"{loc_vbm_dw_match.group(1)} {loc_vbm_dw_match.group(2)} {loc_vbm_dw_match.group(3)}"
        loc_cbm_dw = f"{loc_cbm_dw_match.group(1)} {loc_cbm_dw_match.group(2)} {loc_cbm_dw_match.group(3)}"
        loc_vbm_to = f"{loc_vbm_to_match.group(1)} {loc_vbm_to_match.group(2)} {loc_vbm_to_match.group(3)}"
        loc_cbm_to = f"{loc_cbm_to_match.group(1)} {loc_cbm_to_match.group(2)} {loc_cbm_to_match.group(3)}"


def process_cell_file(filepath):
    global lattice_vectors, ion_positions

    with open(filepath, 'r') as file:
        content = file.read()

        # Используем регулярные выражения для поиска значений
        lattice_vectors_match = re.search(
            r'a1:\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)\n\s*a2:\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)\n\s*a3:\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)',
            content)
        ion_positions_match = re.findall(r'([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)\s*(\w+\d+)', content)

        if lattice_vectors_match:
            # Форматирование значений для переменной lattice_vectors
            lattice_vectors = f"a1: {lattice_vectors_match.group(1)} {lattice_vectors_match.group(2)} {lattice_vectors_match.group(3)}\n"
            lattice_vectors += f"a2: {lattice_vectors_match.group(4)} {lattice_vectors_match.group(5)} {lattice_vectors_match.group(6)}\n"
            lattice_vectors += f"a3: {lattice_vectors_match.group(7)} {lattice_vectors_match.group(8)} {lattice_vectors_match.group(9)}"

        if ion_positions_match:
            # Форматирование значений для переменной ion_positions
            ion_positions = "\n".join(
                [f"{match[0]} {match[1]} {match[2]} {match[3]}" for match in ion_positions_match])
        else:
            ion_positions = None


def process_energy_mag_file(filepath):
    global total_energy, total_magnetization

    with open(filepath, 'r') as file:
        content = file.read()
        print(file.name)
        # Используем регулярные выражения для поиска значений
        total_energy_match = re.search(r'Total energy: ([\d.E+-]+)', content)
        total_magnetization_match = re.search(r'Total magnetization: ([\d.E+-]+)', content)

        if total_energy_match:
            total_energy = float(total_energy_match.group(1))
        else:
            total_energy = None

        if total_magnetization_match:
            total_magnetization = float(total_magnetization_match.group(1))
        else:
            total_magnetization = None


def process_mech_file(filepath):
    global stiffness_tensor, youngs_modulus, shear_modulus, poisson_ratio, bulk_modulus, shear_modulus_mechanical, bulk_shear_ratio

    with open(filepath, 'r') as file:
        content = file.read()
        print(file.name)

        # Используем регулярные выражения для поиска значений
        stiffness_tensor_values = re.search(
            r'Stiffness Tensor C_ij \(in N/m\):\s*([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)',
            content)
        if stiffness_tensor_values:
            stiffness_tensor = [
                [float(stiffness_tensor_values.group(1)), float(stiffness_tensor_values.group(2)),
                 float(stiffness_tensor_values.group(3))],
                [float(stiffness_tensor_values.group(4)), float(stiffness_tensor_values.group(5)),
                 float(stiffness_tensor_values.group(6))],
                [float(stiffness_tensor_values.group(7)), float(stiffness_tensor_values.group(8)),
                 float(stiffness_tensor_values.group(9))]
            ]
        else:
            stiffness_tensor = None

        youngs_modulus_values = re.search(r"Young's Modulus E \(N/m\) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|", content)
        if youngs_modulus_values:
            youngs_modulus = [float(match) for match in youngs_modulus_values.groups()]
        else:
            youngs_modulus = None

        shear_modulus_values = re.search(r"Shear Modulus G \(N/m\) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|", content)
        if shear_modulus_values:
            shear_modulus = [float(match) for match in shear_modulus_values.groups()]
        else:
            shear_modulus = None

        poisson_ratio_values = re.search(r"Poisson's Ratio v \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|", content)
        if poisson_ratio_values:
            poisson_ratio = [float(match) for match in poisson_ratio_values.groups()]
        else:
            poisson_ratio = None

        bulk_modulus_values = re.search(r"Bulk modulus K \(N/m\) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|", content)
        if bulk_modulus_values:
            bulk_modulus = [float(match) for match in bulk_modulus_values.groups()]
        else:
            bulk_modulus = None

        shear_modulus_mechanical_values = re.search(r"Shear modulus G \(N/m\) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|",
                                                    content)
        if shear_modulus_mechanical_values:
            shear_modulus_mechanical = [float(match) for match in shear_modulus_mechanical_values.groups()]
        else:
            shear_modulus_mechanical = None

        bulk_shear_ratio_values = re.search(r"Bulk/Shear ratio \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|", content)
        if bulk_shear_ratio_values:
            bulk_shear_ratio = [float(match) for match in bulk_shear_ratio_values.groups()]
        else:
            bulk_shear_ratio = None


def process_wf_file(filepath):
    global vacuum_level, work_function

    with open(filepath, 'r') as file:
        content = file.read()
        print(file.name)
        # Используем регулярные выражения для поиска значений
        vacuum_level_match = re.search(r'Vacuum-Level \(eV\):\s*([\d.-]+)', content)
        work_function_match = re.search(r'Work Function \(eV\):\s*([\d.-]+)', content)

        if vacuum_level_match:
            vacuum_level = float(vacuum_level_match.group(1))
        else:
            vacuum_level = None

        if work_function_match:
            work_function = float(work_function_match.group(1))
        else:
            work_function = None


def save():
    # Папка, в которой нужно выполнять поиск
    root_dir = 'Base'
    conn = sqlite3.connect('materials.db')

    # Рекурсивно обходим все файлы и папки в указанной директории
    for dirpath, dirnames, filenames in os.walk(root_dir):
        try:
            cursor = conn.cursor()
            for filename in filenames:
                if filename not in ['Structure', 'BANDs', 'Cell', 'Energy_mag_mom', 'Mechanical', 'Work_func']:
                    continue
                if filename == 'Structure':
                    file_path = os.path.join(dirpath, filename)
                    process_structure_file(file_path)
                if filename == 'BANDs':
                    file_path = os.path.join(dirpath, filename)
                    process_bands_file(file_path)
                if filename == 'Cell':
                    file_path = os.path.join(dirpath, filename)
                    process_cell_file(file_path)
                if filename == 'Energy_mag_mom':
                    file_path = os.path.join(dirpath, filename)
                    process_energy_mag_file(file_path)
                if filename == 'Mechanical':
                    file_path = os.path.join(dirpath, filename)
                    process_mech_file(file_path)
                if filename == 'Work_func':
                    file_path = os.path.join(dirpath, filename)
                    process_wf_file(file_path)

            if work_function is None:
                continue

            cursor.execute('''
                INSERT INTO mater (
                    compound,
                    crystal_system,
                    lattice_constants,
                    lattice_angles,
                    layer_thickness,
                    international,
                    space_group,
                    symmetry_operations,
                    band_gap,
                    eigenvalue_vbm,
                    eigenvalue_cbm,
                    fermi_energy,
                    highest_occupied_band,
                    lowest_unoccupied_band,
                    loc_vbm_up,
                    loc_cbm_up,
                    loc_vbm_dw,
                    loc_cbm_dw,
                    loc_vbm_to,
                    loc_cbm_to,
                    lattice_vectors,
                    ion_positions,
                    total_energy,
                    total_magnetization,
                    stiffness_tensor,
                    youngs_modulus,
                    shear_modulus,
                    poisson_ratio,
                    bulk_modulus,
                    shear_modulus_mechanical,
                    bulk_shear_ratio,
                    vacuum_level,
                    work_function
                ) VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?,
                ?, ?,
                ?, ?, ?, ?, ?, ?, ?,
                ?, ?)
            ''', (
                compound,
                crystal_system,
                lattice_constants,
                lattice_angles,
                layer_thickness,
                international,
                space_group,
                symmetry_operations,
                band_gap,
                eigenvalue_vbm,
                eigenvalue_cbm,
                fermi_energy,
                highest_occupied_band,
                lowest_unoccupied_band,
                loc_vbm_up,
                loc_cbm_up,
                loc_vbm_dw,
                loc_cbm_dw,
                loc_vbm_to,
                loc_cbm_to,
                lattice_vectors,
                ion_positions,
                total_energy,
                total_magnetization,
                stiffness_tensor,
                youngs_modulus,
                shear_modulus,
                poisson_ratio,
                bulk_modulus,
                shear_modulus_mechanical,
                bulk_shear_ratio,
                vacuum_level,
                work_function
            ))

            cursor.close()
            # Выполняем коммит, чтобы сохранить изменения в базе данных
            conn.commit()
            print("Data saved successfully")
        except sqlite3.Error as e:
            print(f"Error saving data to the database: {e}")
    conn.close()


if __name__ == "__main__":
    save()
