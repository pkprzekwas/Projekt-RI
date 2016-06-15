import sys
import a_star
import time

try:
    if sys.argv[1] == '1':
        print "Using mode 1"
        import cameraService
except:    
    print "Using mode 2"
    import cameraServiceV2 as cameraService


def main():
    camera = cameraService.startCamera()
    robot = a_star.AStar()
    moves = [(0, 0), (0, 0), (0, 0)]
    try:
        while (True):
            frame = cameraService.getFrameFromCamera(camera=camera)
            error = cameraService.findDirectionError(frame, show=True)
            print robot.read_distance()
            if robot.read_distance() < 3000:
                if all(x == (0,0) for x in moves):
                    robot.play_notes("eee")
                    time.sleep(0.5)
                    robot.motors(-300, 0)
                    time.sleep(3)
                    robot.motors(0, 0)
                    continue
                robot.play_notes("cc")
                time.sleep(0.5)
                robot.motors(-moves[0][0], -moves[0][1])
                time.sleep(1.5)
                robot.motors(0, 0)
                del moves[0]
                moves.append((0, 0))
                if all(x == (0,0) for x in moves):
                    robot.motors(-200, 200)
                    time.sleep(2)
                    robot.motors(0, 0)
                continue
            if error < -0.05:
                robot.motors(0, 300)
                moves.pop()
                moves.insert(0, (0, 300))
                time.sleep(0.5)
            elif error > 0.05:
                robot.motors(300, 0)
                moves.pop()
                moves.insert(0, (300, 0))
                time.sleep(0.5)
            else:
                robot.motors(200, 200)
               # moves.pop()
               # moves.insert(0, (200, 200))
                time.sleep(1.5)
            robot.motors(0, 0)
    finally:
        robot.motors(0, 0)
        camera.close()


if __name__ == "__main__":
    main()
