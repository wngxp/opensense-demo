import os
import opensim as osim

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

MODEL = os.path.join(ROOT, "models", "Rajagopal_2015.osim")
IMU_PLACER_XML = os.path.join(ROOT, "setups", "myIMUPlacer_Setup.xml")
IMU_IK_XML     = os.path.join(ROOT, "setups", "myIMUIK_Setup.xml")

RESULTS_DIR = os.path.join(ROOT, "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

print("Model:", MODEL)
print("IMU Placer setup:", IMU_PLACER_XML)
print("IMU IK setup:", IMU_IK_XML)
print("Results:", RESULTS_DIR)

# --- Step 3: Calibrate model (IMU Placer) ---
placer = osim.IMUPlacer(IMU_PLACER_XML)
placer.set_model_file(MODEL)  # ensures it points at your repo model
placer.run(True)

print("✅ IMU Placer finished.")

# --- Step 4: IMU Inverse Kinematics ---
ik = osim.IMUInverseKinematicsTool(IMU_IK_XML)
ik.set_model_file(MODEL)  # ensures it points at your repo model
ik.run()

print("✅ IMU IK finished.")
