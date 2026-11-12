import os

ROBOT = "g1" # Robot name, "go2", "b2", "b2w", "h1", "go2w", "g1" 
# G1 model, chosen with BIORL_G1_ROBOT (bioRL-lab robot names): g1_23dof (default) or
# g1_29dof / g1_29dof_locked / g1_29dof_waist (all use the 29-DOF MJCF).
G1_MODEL = "g1_29dof" if os.environ.get("BIORL_G1_ROBOT", "g1_23dof").startswith("g1_29dof") else "g1_23dof"
# Reported in LowState.mode_machine, like the real robot (4 = 23-DOF, 5 = 29-DOF);
# deploy_unitree_mujoco.py refuses to drive a model that doesn't match the policy.
G1_MODE_MACHINE = {"g1_23dof": 4, "g1_29dof": 5}[G1_MODEL]
ROBOT_SCENE = "../unitree_robots/" + ROBOT + ("/scene_" + G1_MODEL[3:] + ".xml" if ROBOT == "g1" else "/scene.xml")

DOMAIN_ID = 0 # Domain id
INTERFACE = "lo" # Interface 

USE_JOYSTICK = int(os.environ.get("UNITREE_SIM_JOYSTICK", "1")) # Simulate Unitree WirelessController using a gamepad (UNITREE_SIM_JOYSTICK=0: none connected)
JOYSTICK_TYPE = "xbox" # support "xbox" and "switch" gamepad layout
JOYSTICK_DEVICE = 0 # Joystick number

PRINT_SCENE_INFORMATION = True # Print link, joint and sensors information of robot
ENABLE_ELASTIC_BAND = True # Virtual spring band, used for lifting h1/g1 (keys: 7/8 shorten/lengthen, 9 release)
# Initial band length [m]: 0.6 leaves the G1's feet loaded on the ground (0 = hanging in the air).
ELASTIC_BAND_LENGTH = 0.6
# With USE_JOYSTICK: LB lowers (lengthens) the band, RB raises it, Y releases / re-attaches it.

SIMULATE_DT = 0.005  # Need to be larger than the runtime of viewer.sync()
VIEWER_DT = 0.02  # 50 fps for viewer
