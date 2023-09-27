import os
import re
import sqlite3


def a_h():
    def process_file(filepath, output_file):
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

            # Вставляем запись в таблицу Materials
            try:
                cursor.execute('''
                            INSERT INTO Materials (
                                Prototype, TotalAtoms, FormulaUnit, FullFormulaUnit, TwoDCrystalSystem, LatticeConstants, 
                                LatticeAngles, LayerThickness, International, SpaceGroup, SymmetryOperations
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            ''',
                               (prototype, total_atoms, formula_unit, full_formula_unit, crystal_system,
                                lattice_constants,
                                lattice_angles, layer_thickness, international, space_group, symmetry_operations))
                print("Saved with no errors(a_h)")
            except sqlite3.Error as e:
                print(f"Error saving to database(a_h): {e}")

    # Папка, в которой нужно выполнять поиск
    root_dir = 'Base'

    # Путь к файлу вывода
    output_file = 'a_h.txt'

    # Очищаем содержимое файла вывода перед началом
    with open(output_file, 'w') as out_file:
        out_file.write('')

    # Рекурсивно обходим все файлы и папки в указанной директории
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'a_h':
                file_path = os.path.join(dirpath, filename)
                process_file(file_path, output_file)


def bands():
    # Функция для извлечения значений и записи их в файл
    def process_bands_file(filepath, output_file):
        with open(filepath, 'r') as file:
            content = file.read()

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

            # Вставляем запись в таблицу Materials
        try:
            cursor.execute('''
                            INSERT INTO Materials (
                                BandGap_eV, EigenvalueVBM_eV, EigenvalueCBM_eV, FermiEnergy_eV,
                                HighestOccupiedBand, LowestUnoccupiedBand,
                                LocationVBM_UP, LocationCBM_UP, LocationVBM_DW, LocationCBM_DW, LocationVBM_TO, LocationCBM_TO
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            ''', (f'{band_gap.group(1)} {band_gap.group(2)} {band_gap.group(3)}',
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
                                  f'{location_cbm_to.group(1)} {location_cbm_to.group(2)} {location_cbm_to.group(3)}'))
            print("Saved with no errors(bands)")
        except sqlite3.Error as e:
            print(f"Error saving to database(bands): {e}")

    # Папка, в которой нужно выполнять поиск
    root_dir = 'Base'

    # Путь к файлу вывода
    output_file = 'bands.txt'

    # Очищаем содержимое файла вывода перед началом
    with open(output_file, 'w') as out_file:
        out_file.write('')

    # Рекурсивно обходим все файлы и папки в указанной директории
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'bands':
                file_path = os.path.join(dirpath, filename)
                process_bands_file(file_path, output_file)


def bands_nc():
    # Функция для извлечения значений и записи их в файл
    def process_bands_nc_file(filepath, output_file):
        with open(filepath, 'r') as file:
            content = file.read()

            # Используем регулярные выражения для поиска значений
            band_character = re.search(r'Band Character:\s*(\w+)', content).group(1)
            band_gap = re.search(r'Band Gap \(eV\):\s*([\d.-]+)', content).group(1)
            eigenvalue_vbm = re.search(r'Eigenvalue of VBM \(eV\):\s*([\d.-]+)', content).group(1)
            eigenvalue_cbm = re.search(r'Eigenvalue of CBM \(eV\):\s*([\d.-]+)', content).group(1)
            fermi_energy = re.search(r'Fermi Energy \(eV\):\s*([\d.-]+)', content).group(1)
            homo_lumo_bands = re.search(r'HOMO & LUMO Bands:\s*(\d+)\s*(\d+)', content)
            location_vbm = re.search(r'Location of VBM:\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)
            location_cbm = re.search(r'Location of CBM:\s*([\d.-]+)\s*([\d.-]+)\s*([\d.-]+)', content)

        try:
            # Вставляем запись в таблицу Materials
            cursor.execute('''
                INSERT INTO Materials (
                    BandCharacter, BandGap_double, EigenvalueVBM_double, EigenvalueCBM_double, FermiEnergy_double,
                    HOMO_LUMO_Bands,
                    LocationVBM, LocationCBM
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                band_character, float(band_gap), float(eigenvalue_vbm), float(eigenvalue_cbm), float(fermi_energy),
                homo_lumo_bands.group(0) if homo_lumo_bands else None,
                location_vbm.group(0), location_cbm.group(0)))
            print("Saved with no errors(bands_nc)")
        except sqlite3.Error as e:
            print(f"Error saving to database(bands_nc): {e}")

    # Папка, в которой нужно выполнять поиск
    root_dir = 'Base'

    # Путь к файлу вывода
    output_file = 'bands_nc.txt'

    # Очищаем содержимое файла вывода перед началом
    with open(output_file, 'w') as out_file:
        out_file.write('')

    # Рекурсивно обходим все файлы и папки в указанной директории
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'bands_nc':
                file_path = os.path.join(dirpath, filename)
                process_bands_nc_file(file_path, output_file)


def energy_mag():
    # Функция для извлечения значений и записи их в файл
    def process_energy_mag_file(filepath, output_file):
        with open(filepath, 'r') as file:
            content = file.read()

            # Используем регулярные выражения для поиска значений
            f_value = re.search(r'F= ([\d.E+-]+)', content).group(1)
            e0_value = re.search(r'E0= ([\d.E+-]+)', content).group(1)
            e_value = re.search(r'd E =([\d.E+-]+)', content).group(1)
            mag_value = re.search(r'mag= ([\d.E+-]+)', content).group(1)

        # Вставляем запись в таблицу Materials
        try:
            cursor.execute('''
                            INSERT INTO Materials (
                                F, E0, E, mag
                            ) VALUES (?, ?, ?, ?)
                            ''', (f_value, e0_value, e_value, float(mag_value)))
            print("Saved with no errors(energy_mag)")
        except sqlite3.Error as e:
            print(f"Error saving to database(energy_mag): {e}")

    # Папка, в которой нужно выполнять поиск
    root_dir = 'Base'

    # Путь к файлу вывода
    output_file = 'energy_mag.txt'

    # Очищаем содержимое файла вывода перед началом
    with open(output_file, 'w') as out_file:
        out_file.write('')

    # Рекурсивно обходим все файлы и папки в указанной директории
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'energy_mag':
                file_path = os.path.join(dirpath, filename)
                process_energy_mag_file(file_path, output_file)


def wf():
    # Функция для извлечения значений и записи их в файл
    def process_wf_file(filepath, output_file):
        with open(filepath, 'r') as file:
            content = file.read()

            # Используем регулярные выражения для поиска значений
            vacuum_level = re.search(r'Vacuum-Level \(eV\):\s*([\d.]+)', content).group(1)
            work_function = re.search(r'Work Function \(eV\):\s*([\d.]+)', content).group(1)

        try:
            # Вставляем запись в таблицу Materials
            cursor.execute('''
                        INSERT INTO Materials (
                            VacuumLevel_eV, WorkFunction_eV
                        ) VALUES (?, ?)
                        ''', (float(vacuum_level), float(work_function)))
            print("Saved with no errors(wf)")
        except sqlite3.Error as e:
            print(f"Error saving to database(wf): {e}")

    # Папка, в которой нужно выполнять поиск
    root_dir = 'Base'

    # Путь к файлу вывода
    output_file = 'wf.txt'

    # Очищаем содержимое файла вывода перед началом
    with open(output_file, 'w') as out_file:
        out_file.write('')

    # Рекурсивно обходим все файлы и папки в указанной директории
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'wf':
                file_path = os.path.join(dirpath, filename)
                process_wf_file(file_path, output_file)


if __name__ == "__main__":
    # Создаем подключение к базе данных SQLite
    conn = sqlite3.connect('materials.db')
    cursor = conn.cursor()

    a_h()
    bands()
    bands_nc()
    energy_mag()
    wf()
