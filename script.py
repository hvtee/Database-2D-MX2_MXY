import os
import re
import sqlite3

# a_h
prototype = None
total_atoms = None
formula_unit = None
full_formula_unit = None
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
location_vbm_up = None
location_cbm_up = None
location_vbm_dw = None
location_cbm_dw = None
location_vbm_to = None
location_cbm_to = None

# bands_nc
band_character_nc = None
band_gap_nc = None
eigenvalue_vbm_nc = None
eigenvalue_cbm_nc = None
fermi_energy_nc = None
homo_lumo_bands_nc = None
location_vbm_nc = None
location_cbm_nc = None

# cell
cell_values = None

# energy_mag
f_value = None
e0_value = None
e_value = None
mag_value = None

# mech
CrystalSystem = None
StiffnessTensor = None
ComplianceTensor = None
YoungsModulus = None
ShearModulusAnis = None
PoissonsRatio = None
BulkModulus = None
ShearModulusAver = None
BulkShearRatio = None
ASU = None
AKube = None
KVRatio = None
GVRatio = None

# wf
vacuum_level = None
work_function = None


def process_file(filepath):
    global prototype, total_atoms, formula_unit, full_formula_unit, crystal_system
    global lattice_constants, lattice_angles, layer_thickness, international, space_group, symmetry_operations

    # Функция для извлечения значений и записи их в файл
    with open(filepath, 'r') as file:
        content = file.read()
        print(file.name)
        # Используем регулярные выражения для поиска значений
        prototype = re.search(r'Prototype:\s*(\w+)', content).group(1)
        total_atoms = re.search(r'Total-Atoms:\s*(\d+)', content).group(1)
        formula_unit = re.search(r'Formula-Unit:\s*([^[\]]+)', content).group(1)
        full_formula_unit = re.search(r'Full Formula-Unit:\s*(\S+)', content).group(1)
        crystal_system = re.search(r'2D Crystal System:\s*(\w+)', content).group(1)
        lattice_constants = re.search(r'Lattice Constants:\s*([\d. ]+)', content).group(1)
        lattice_angles = re.search(r'Lattice Angles:\s*([\d. ]+)', content).group(1)
        layer_thickness = re.search(r'Layer Thickness:\s*([\d.]+)', content).group(1)
        international = re.search(r'International:\s*(\S+)', content).group(1)
        space_group = re.search(r'Space Group:\s*(\d+)', content).group(1)
        symmetry_operations = re.search(r'Symmetry Operations:\s*(\d+)', content).group(1)


def process_bands_file(filepath):
    global band_gap, eigenvalue_vbm, eigenvalue_cbm, fermi_energy
    global highest_occupied_band, lowest_unoccupied_band
    global location_vbm_up, location_cbm_up, location_vbm_dw, location_cbm_dw
    global location_vbm_to, location_cbm_to

    with open(filepath, 'r') as file:
        content = file.read()
        print(file.name)
        # Используем регулярные выражения для поиска значений
        band_gap = re.search(r'Band Gap \(eV\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        eigenvalue_vbm = re.search(r'Eigenvalue of VBM \(eV\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        eigenvalue_cbm = re.search(r'Eigenvalue of CBM \(eV\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        fermi_energy = re.search(r'Fermi Energy \(eV\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        highest_occupied_band = re.search(r'Highest-Occupied Band:\s*(\d+)\s*(\d+)\s*(\d+)', content)
        lowest_unoccupied_band = re.search(r'Lowest-Unoccupied Band:\s*(\d+)\s*(\d+)\s*(\d+)', content)
        location_vbm_up = re.search(r'Location of VBM \(UP\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        location_cbm_up = re.search(r'Location of CBM \(UP\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        location_vbm_dw = re.search(r'Location of VBM \(DW\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        location_cbm_dw = re.search(r'Location of CBM \(DW\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        location_vbm_to = re.search(r'Location of VBM \(TO\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
        location_cbm_to = re.search(r'Location of CBM \(TO\):\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)


def process_bands_nc_file(filepath):
    global band_character_nc, band_gap_nc, eigenvalue_vbm_nc, eigenvalue_cbm_nc, fermi_energy_nc
    global homo_lumo_bands_nc, location_vbm_nc, location_cbm_nc

    with open(filepath, 'r') as file:
        content = file.read()
        print(file.name)
        # Используем регулярные выражения для поиска значений
        band_character_nc = re.search(r'Band Character:\s*(\w+)', content).group(1)
        band_gap_nc = float(re.search(r'Band Gap \(eV\):\s*([\d.-]+)', content).group(1))
        eigenvalue_vbm_nc = float(re.search(r'Eigenvalue of VBM \(eV\):\s*([\d.-]+)', content).group(1))
        eigenvalue_cbm_nc = float(re.search(r'Eigenvalue of CBM \(eV\):\s*([\d.-]+)', content).group(1))
        fermi_energy_nc = float(re.search(r'Fermi Energy \(eV\):\s*([\d.-]+)', content).group(1))
        homo_lumo_bands_nc = tuple(map(int, re.search(r'HOMO & LUMO Bands:\s*(\d+)\s*(\d+)', content).groups()))
        location_vbm_nc = tuple(
            map(float, re.search(r'Location of VBM:\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content).groups()))
        location_cbm_nc = tuple(
            map(float, re.search(r'Location of CBM:\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content).groups()))


def process_cell_file(filepath):
    global cell_values

    with open(filepath, 'r') as file:
        content = file.read()

        # Используем регулярное выражение для поиска строк под "Direct" и извлекаем координаты и метки
        pattern = r'Direct\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+(\w+\d+)\n\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+(\w+\d+)\n\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+(\w+\d+)'
        cell_tuples = re.findall(pattern, content)
    if cell_tuples:
        # Преобразуем строки с координатами и метками в кортежи значений
        cell_values = [
            (float(cell_tuples[0][0]), float(cell_tuples[0][1]), float(cell_tuples[0][2]), cell_tuples[0][3]),
            (float(cell_tuples[0][4]), float(cell_tuples[0][5]), float(cell_tuples[0][6]), cell_tuples[0][7]),
            (float(cell_tuples[0][8]), float(cell_tuples[0][9]), float(cell_tuples[0][10]), cell_tuples[0][11])
        ]
    else:
        cell_values = None


def process_energy_mag_file(filepath):
    global f_value, e0_value, e_value, mag_value

    with open(filepath, 'r') as file:
        content = file.read()
        print(file.name)
        # Используем регулярные выражения для поиска значений
        f_value = re.search(r'F= ([\d.E+-]+)', content).group(1)
        e0_value = re.search(r'E0= ([\d.E+-]+)', content).group(1)
        e_value = re.search(r'd E =([\d.E+-]+)', content).group(1)
        mag_value = re.search(r'mag= ([\d.E+-]+)', content).group(1)


def process_mech_file(filepath):
    global CrystalSystem, StiffnessTensor, ComplianceTensor
    global YoungsModulus, ShearModulusAnis, PoissonsRatio
    global BulkModulus, ShearModulusAver, BulkShearRatio
    global ASU, AKube, KVRatio, GVRatio

    with open(filepath, 'r') as file:
        content = file.read()
        print(file.name)

        #####
        CrystalSystem_value = re.search(r'Crystal System:\s+(\w+)', content)
        if CrystalSystem_value:
            CrystalSystem = CrystalSystem_value.group(1)
        else:
            CrystalSystem = None

        #####
        StiffnessTensor_values = re.search(
            r'Stiffness Tensor C_ij \(in N/m\):\s*([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)',
            content)
        if StiffnessTensor_values:
            StiffnessTensor = [
                [float(StiffnessTensor_values.group(1)), float(StiffnessTensor_values.group(2)),
                 float(StiffnessTensor_values.group(3))],
                [float(StiffnessTensor_values.group(4)), float(StiffnessTensor_values.group(5)),
                 float(StiffnessTensor_values.group(6))],
                [float(StiffnessTensor_values.group(7)), float(StiffnessTensor_values.group(8)),
                 float(StiffnessTensor_values.group(9))]
            ]
        else:
            StiffnessTensor = None

        #####
        ComplianceTensor_values = re.search(
            r'Compliance Tensor S_ij \(in m/N\):\s*([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)',
            content)
        if ComplianceTensor_values:
            ComplianceTensor = [
                [float(ComplianceTensor_values.group(1)), float(ComplianceTensor_values.group(2)),
                 float(ComplianceTensor_values.group(3))],
                [float(ComplianceTensor_values.group(4)), float(ComplianceTensor_values.group(5)),
                 float(ComplianceTensor_values.group(6))],
                [float(ComplianceTensor_values.group(7)), float(ComplianceTensor_values.group(8)),
                 float(ComplianceTensor_values.group(9))]
            ]
        else:
            ComplianceTensor = None

        #####
        YoungsModulus = re.search(r"Young's Modulus E \(N/m\) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|", content)
        if YoungsModulus:
            YoungsModulus = [float(match) for match in YoungsModulus.groups()]
        else:
            YoungsModulus = None

        #####
        ShearModulusAnis = re.search(r"Shear Modulus G \(N/m\) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|", content)
        if ShearModulusAnis:
            ShearModulusAnis = [float(match) for match in ShearModulusAnis.groups()]
        else:
            ShearModulusAnis = None

        #####
        PoissonsRatio = re.search(r"Poisson's Ratio v \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|", content)
        if PoissonsRatio:
            PoissonsRatio = [float(match) for match in PoissonsRatio.groups()]
        else:
            PoissonsRatio = None

        BulkModulus = re.search(r"Bulk modulus K \(N/m\) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|", content)
        if BulkModulus:
            BulkModulus = [float(match) for match in BulkModulus.groups()]
        else:
            BulkModulus = None

        ShearModulusAver = re.search(r"Shear modulus G \(N/m\) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|", content)
        if ShearModulusAver:
            ShearModulusAver = [float(match) for match in ShearModulusAver.groups()]
        else:
            ShearModulusAver = None

        BulkShearRatio = re.search(r"Bulk/Shear ratio \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|", content)
        if BulkShearRatio:
            BulkShearRatio = [float(match) for match in BulkShearRatio.groups()]
        else:
            BulkShearRatio = None

        ASU = re.search(r'Universal Elastic Anisotropy Index \(A_SU\):\s+([\d.-]+)', content)
        if ASU:
            ASU = ASU.group(1)
        else:
            ASU = None

        AKube = re.search(r'Kube Anisotropy Index \(A_Kube\):\s+([\d.-]+)', content)
        if AKube:
            AKube = AKube.group(1)
        else:
            AKube = None

        KVRatio = re.search(r'K_V/K_R Ratio:\s+([\d.-]+)', content)
        if KVRatio:
            KVRatio = KVRatio.group(1)
        else:
            KVRatio = None

        GVRatio = re.search(r'G_V/G_R Ratio:\s+([\d.-]+)', content)
        if GVRatio:
            GVRatio = GVRatio.group(1)
        else:
            GVRatio = None


def process_wf_file(filepath):
    global vacuum_level, work_function

    with open(filepath, 'r') as file:
        content = file.read()
        print(file.name)
        # Используем регулярные выражения для поиска значений
        vacuum_level = re.search(r'Vacuum-Level \(eV\):\s*([\d.]+)', content).group(1)
        work_function = re.search(r'Work Function \(eV\):\s*([\d.]+)', content).group(1)


def save():
    # Папка, в которой нужно выполнять поиск
    root_dir = 'Base'
    conn = sqlite3.connect('materials.db')

    # Рекурсивно обходим все файлы и папки в указанной директории
    for dirpath, dirnames, filenames in os.walk(root_dir):
        try:
            cursor = conn.cursor()
            for filename in filenames:
                if filename not in ['a_h', 'bands', 'bands_nc', 'cell', 'energy_mag', 'mech', 'wf']:
                    continue
                if filename == 'a_h':
                    file_path = os.path.join(dirpath, filename)
                    process_file(file_path)
                if filename == 'bands':
                    file_path = os.path.join(dirpath, filename)
                    process_bands_file(file_path)
                if filename == 'bands_nc':
                    file_path = os.path.join(dirpath, filename)
                    process_bands_nc_file(file_path)
                if filename == 'cell':
                    file_path = os.path.join(dirpath, filename)
                    process_cell_file(file_path)
                if filename == 'energy_mag':
                    file_path = os.path.join(dirpath, filename)
                    process_energy_mag_file(file_path)
                if filename == 'mech':
                    file_path = os.path.join(dirpath, filename)
                    process_mech_file(file_path)
                if filename == 'wf':
                    file_path = os.path.join(dirpath, filename)
                    process_wf_file(file_path)

            if work_function is None:
                continue

            cursor.execute('''
                INSERT INTO Materials (
                    Prototype, 
                    TotalAtoms, 
                    FormulaUnit, 
                    FullFormulaUnit, 
                    TwoDCrystalSystem,
                    LatticeConstants, 
                    LatticeAngles, 
                    LayerThickness, 
                    International, 
                    SpaceGroup,
                    SymmetryOperations, 
                    BandGap_eV, 
                    EigenvalueVBM_eV, 
                    EigenvalueCBM_eV,
                    FermiEnergy_eV, 
                    HighestOccupiedBand, 
                    LowestUnoccupiedBand, 
                    LocationVBM_UP,
                    LocationCBM_UP, 
                    LocationVBM_DW, 
                    LocationCBM_DW, 
                    LocationVBM_TO, 
                    LocationCBM_TO,
                    BandCharacterNC, 
                    BandGapNC, 
                    EigenvalueVBMNC, 
                    EigenvalueCBMNC, 
                    FermiEnergyNC,
                    HOMO_LUMO_BandsNC, 
                    LocationVBMNC, 
                    LocationCBMNC,  
                    CellDirect,
                    F, 
                    E0, 
                    E, 
                    mag,
                    CrystalSystem,
                    StiffnessTensor, 
                    ComplianceTensor, 
                    YoungsModulus, 
                    ShearModulusAnis, 
                    PoissonsRatio, 
                    BulkModulus, 
                    ShearModulusAver,
                    BulkShearRatio, 
                    ASU, 
                    AKube, 
                    KVRatio,
                    GVRatio,
                    VacuumLevel_eV, 
                    WorkFunction_eV
                ) VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?,
                ?,
                ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?)
            ''', (
                prototype,
                total_atoms,
                formula_unit,
                full_formula_unit,
                crystal_system,
                lattice_constants,
                lattice_angles,
                layer_thickness,
                international,
                space_group,
                symmetry_operations,
                f'{band_gap.group(1)} {band_gap.group(2)} {band_gap.group(3)}',
                f'{eigenvalue_vbm.group(1)} {eigenvalue_vbm.group(2)} {eigenvalue_vbm.group(3)}',
                f'{eigenvalue_cbm.group(1)} {eigenvalue_cbm.group(2)} {eigenvalue_cbm.group(3)}',
                f'{fermi_energy.group(1)} {fermi_energy.group(2)} {fermi_energy.group(3)}',
                f'{highest_occupied_band.group(1)} {highest_occupied_band.group(2)} {highest_occupied_band.group(3)}',
                f'{lowest_unoccupied_band.group(1)} {lowest_unoccupied_band.group(2)} {lowest_unoccupied_band.group(3)}',
                f'{location_vbm_up.group(1)} {location_vbm_up.group(2)} {location_vbm_up.group(3)}',
                f'{location_cbm_up.group(1)} {location_cbm_up.group(2)} {location_cbm_up.group(3)}',
                f'{location_vbm_dw.group(1)} {location_vbm_dw.group(2)} {location_vbm_dw.group(3)}',
                f'{location_cbm_dw.group(1)} {location_cbm_dw.group(2)} {location_cbm_dw.group(3)}',
                f'{location_vbm_to.group(1)} {location_vbm_to.group(2)} {location_vbm_to.group(3)}',
                f'{location_cbm_to.group(1)} {location_cbm_to.group(2)} {location_cbm_to.group(3)}',
                band_character_nc,
                float(band_gap_nc),
                float(eigenvalue_vbm_nc),
                float(eigenvalue_cbm_nc),
                float(fermi_energy_nc),
                f'{homo_lumo_bands_nc[0]} {homo_lumo_bands_nc[1]}',
                f'{location_vbm_nc[0]} {location_vbm_nc[1]} {location_vbm_nc[2]}',
                f'{location_cbm_nc[0]} {location_cbm_nc[1]} {location_cbm_nc[2]}',
                str(cell_values),
                f_value,
                e0_value,
                e_value,
                float(mag_value),
                str(CrystalSystem),
                str(StiffnessTensor),
                str(ComplianceTensor),
                str(YoungsModulus),
                str(ShearModulusAnis),
                str(PoissonsRatio),
                str(BulkModulus),
                str(ShearModulusAver),
                str(BulkShearRatio),
                str(ASU),
                str(AKube),
                str(KVRatio),
                str(GVRatio),
                float(vacuum_level),
                float(work_function)))

            cursor.close()
            # Выполняем коммит, чтобы сохранить изменения в базе данных
            conn.commit()
            print("Data saved successfully")
        except sqlite3.Error as e:
            print(f"Error saving data to the database: {e}")
    conn.close()


if __name__ == "__main__":
    save()
