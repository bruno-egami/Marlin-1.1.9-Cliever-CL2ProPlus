import re

conf_path = r"d:\GitHub\Marlin-1.1.9.1-Cliever-CL2ProPlus\Marlin\Configuration.h"

with open(conf_path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    (r'^#define MOTHERBOARD\s+.*$', r'#define MOTHERBOARD BOARD_PRINTRBOARD'),
    (r'^#define TEMP_SENSOR_0\s+.*$', r'#define TEMP_SENSOR_0 998'),
    (r'^#define TEMP_SENSOR_BED\s+.*$', r'#define TEMP_SENSOR_BED 0'),
    (r'^#define PREVENT_COLD_EXTRUSION.*$', r'//#define PREVENT_COLD_EXTRUSION'),
    (r'^#define EXTRUDE_MINTEMP\s+.*$', r'#define EXTRUDE_MINTEMP 0'),
    (r'^//#define COREXY.*$', r'#define COREXY'),
    (r'^#define USE_XMIN_PLUG.*$', r'//#define USE_XMIN_PLUG'),
    (r'^//#define USE_XMAX_PLUG.*$', r'#define USE_XMAX_PLUG'),
    (r'^#define USE_YMIN_PLUG.*$', r'#define USE_YMIN_PLUG'),
    (r'^//#define USE_ZMAX_PLUG.*$', r'#define USE_ZMAX_PLUG'),
    (r'^#define USE_ZMIN_PLUG.*$', r'//#define USE_ZMIN_PLUG'),
    (r'^#define INVERT_Y_DIR\s+.*$', r'#define INVERT_Y_DIR false'),
    (r'^#define X_HOME_DIR\s+.*$', r'#define X_HOME_DIR 1'),
    (r'^#define Z_HOME_DIR\s+.*$', r'#define Z_HOME_DIR 1'),
    (r'^#define X_BED_SIZE\s+.*$', r'#define X_BED_SIZE 300'),
    (r'^#define Y_BED_SIZE\s+.*$', r'#define Y_BED_SIZE 226'),
    (r'^#define Z_MAX_POS\s+.*$', r'#define Z_MAX_POS 400'),
    (r'^#define DEFAULT_AXIS_STEPS_PER_UNIT\s+\{.*$', r'#define DEFAULT_AXIS_STEPS_PER_UNIT   { 53.33, 53.33, 800.0, 93.88 }'),
    (r'^#define DEFAULT_MAX_FEEDRATE\s+\{.*$', r'#define DEFAULT_MAX_FEEDRATE          { 500, 500, 10, 45 }'),
    (r'^#define DEFAULT_MAX_ACCELERATION\s+\{.*$', r'#define DEFAULT_MAX_ACCELERATION      { 9000, 7000, 100, 10000 }'),
    (r'^#define DEFAULT_ACCELERATION\s+\d+.*$', r'#define DEFAULT_ACCELERATION          2000    // X, Y, Z and E acceleration for printing moves'),
    (r'^#define DEFAULT_RETRACT_ACCELERATION\s+\d+.*$', r'#define DEFAULT_RETRACT_ACCELERATION  3000    // E acceleration for retracts'),
    (r'^#define DEFAULT_XJERK\s+.*$', r'#define DEFAULT_XJERK                 20.0'),
    (r'^#define DEFAULT_YJERK\s+.*$', r'#define DEFAULT_YJERK                 20.0'),
    (r'^#define DEFAULT_ZJERK\s+.*$', r'#define DEFAULT_ZJERK                  0.4'),
    (r'^#define DEFAULT_EJERK\s+.*$', r'#define DEFAULT_EJERK                  5.0'),
    (r'^#define HOMING_FEEDRATE_Z\s+\(4\*60\).*$', r'#define HOMING_FEEDRATE_Z  (12*60)'),
    (r'^//#define EEPROM_SETTINGS.*$', r'#define EEPROM_SETTINGS'),
    (r'^//#define SDSUPPORT.*$', r'#define SDSUPPORT'),
    (r'^//#define ULTIMAKERCONTROLLER.*$', r'#define ULTIMAKERCONTROLLER')
]

for pat, rep in replacements:
    match = re.search(pat, text, flags=re.MULTILINE)
    if not match:
        print(f"FAILED TO MATCH: {pat}")
    text = re.sub(pat, rep, text, flags=re.MULTILINE)

with open(conf_path, 'w', encoding='utf-8') as f:
    f.write(text)

adv_path = r"d:\GitHub\Marlin-1.1.9.1-Cliever-CL2ProPlus\Marlin\Configuration_adv.h"
with open(adv_path, 'r', encoding='utf-8') as f:
    adv_text = f.read()

adv_replacements = [
    (r'^#define X_HOME_BUMP_MM\s+.*$', r'#define X_HOME_BUMP_MM 5'),
    (r'^#define Y_HOME_BUMP_MM\s+.*$', r'#define Y_HOME_BUMP_MM 5'),
    (r'^#define Z_HOME_BUMP_MM\s+.*$', r'#define Z_HOME_BUMP_MM 5')
]

for pat, rep in adv_replacements:
    match = re.search(pat, adv_text, flags=re.MULTILINE)
    if not match:
        print(f"FAILED TO MATCH ADV: {pat}")
    adv_text = re.sub(pat, rep, adv_text, flags=re.MULTILINE)

with open(adv_path, 'w', encoding='utf-8') as f:
    f.write(adv_text)

print("Patching complete.")
