ROBOT = "g1" # Robot name, "go2", "b2", "b2w", "h1", "go2w", "g1" 
#ROBOT_SCENE = "../unitree_robots/" + ROBOT + "/scene_29dof.xml" # Robot scene
ROBOT_SCENE = "../unitree_robots/" + ROBOT + "/scene_23dof.xml" # Robot scene (bioRL-lab policies are G1-23DOF)

DOMAIN_ID = 0 # Domain id
INTERFACE = "lo" # Interface 

USE_JOYSTICK = 1 # Simulate Unitree WirelessController using a gamepad
JOYSTICK_TYPE = "xbox" # support "xbox" and "switch" gamepad layout
JOYSTICK_DEVICE = 0 # Joystick number

PRINT_SCENE_INFORMATION = True # Print link, joint and sensors information of robot
ENABLE_ELASTIC_BAND = True # Virtual spring band, used for lifting h1/g1 (keys: 7/8 shorten/lengthen, 9 release)
# Initial band length [m]: 0.6 leaves the G1's feet loaded on the ground (0 = hanging in the air).
ELASTIC_BAND_LENGTH = 0.6
# With USE_JOYSTICK: LB lowers (lengthens) the band, RB raises it, Y releases / re-attaches it.

SIMULATE_DT = 0.005  # Need to be larger than the runtime of viewer.sync()
VIEWER_DT = 0.02  # 50 fps for viewer
