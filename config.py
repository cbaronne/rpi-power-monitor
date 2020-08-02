import logging
import sys

# Create basic logger
logger = logging.getLogger('power_monitor')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
logger.addHandler(ch)


# Using a multimeter, measure the voltage of the receptacle where your 9V AC transformer will plug into. Enter the measured value below.
GRID_VOLTAGE = 123.7
# Using a multimeter, measure the output voltage of your AC transformer. Using the value on the label is not ideal and will lead to greater accuracy in the calculations.
AC_TRANSFORMER_OUTPUT_VOLTAGE = 10.75


# Define Variables
ct0_channel = 0             # Orange Pair           | House main (leg 1 - left)  (orange pair)
ct1_channel = 1             # Green Pair            | House main (leg 2 - right) (green pair)
ct2_channel = 2             # Blue Pair             | Subpanel main (leg 1 - top)
ct3_channel = 3             # Brown Pair            | Solar Power 
ct4_channel = 6             # 3.5mm Input #1        | Subpanel main (leg 2 - bottom)
board_voltage_channel =  4  # Board voltage ~3.3V
v_sensor_channel = 5        # 9V AC Voltage channel
ct5_channel = 7             # 3.5mm Input #2        | Unused

# The values from running the software in "phase" mode should go below!
ct_phase_correction = {
    'ct0' : 1.03049130,
    'ct1' : 1.06096664,
    'ct2' : 1.69054096,
    'ct3' : 1.50650598,
    'ct4' : 1.02809211,
    'ct5' : 1.77448827,
}

# AFTER phase correction is completed, these values are used in the final calibration for accuracy. See the documentation for more information.
accuracy_calibration = {
    'ct0' : 0.99458943,
    'ct1' : 1,
    'ct2' : 1.08555779,
    'ct3' : 1.13058419,
    'ct4' : 0.91085271,
    'ct5' : 0.96507438,
    'AC'  : 1.07573350,
}
