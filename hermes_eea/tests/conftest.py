import os

from hermes_eea.Stepper.StepperTable import StepperTable
from hermes_eea.calibration.calibration import (
    STEPPER_TABLE_FOR_FILE,
    get_stepper_table_for_file,
    get_apid_for_file,
)

TEST_PROCESSING = [
   "boot_packet.txt",
   "hermes_EEA_l0_2026161-132236_v0.bin",
   "boot_packet.txt",
   "hermes_EEA_l0_2026161-132237_v0.bin",
   "boot_packet.txt",
   "hermes_EEA_hk_l0_2026161-132237_v0.bin",
   "boot_packet.txt",
   "hermes_EEA_hk_l0_2026023-000000_v0.bin",
   "boot_packet.txt",
   "hermes_EEA_l0_2026023-000000_v0.bin",
   "boot_packet.txt",
   "hermes_EEA_l0_2023042-000000_v0.bin"
      
]
    

# STEPPER_TABLE_FOR_FILE, get_stepper_table_for_file, and get_apid_for_file now live in
# hermes_eea.calibration.calibration (the production module) and are re-exported here so
# process_file() and the tests share a single registry instead of drifting out of sync.

