from cflib.positioning.motion_commander import MotionCommander
URI = 'radio://0/80/2M'
if __name__ == "__main__":
    mp = MotionCommander(URI)
    mp.take_off(height=0.3, velocity=0.2)
    mp.land(velocity=0.2)
