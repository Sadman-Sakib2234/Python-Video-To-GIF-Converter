import imageio
import os
import time

clip = os.path.abspath('video.mp4')


def gifmaker(inputPath, targetPath):
    outputPath = os.path.splitext(inputPath)[0] + targetPath

    print(f'Converting { inputPath } \n to { outputPath }')

    render = imageio.get_reader(inputPath)
    fps = render.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath, fps=fps)

    for frames in render:
        writer.append_data(frames)
        print(f'Frame {frames}')
    print("Done!")
    print("Created By- Sadman Sakib")
    writer.close()
    time.sleep(3.5)


gifmaker(clip, '.gif')
