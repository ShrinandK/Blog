from moviepy.editor import *

inputVideoPathOne = 'input_videos/video_1.mp4'
inputVideoPathTwo = 'output_videos/video_1.avi'
outputVideoPathOne = 'output_videos/vid_1_input.gif'
outputVideoPathTwo = 'output_videos/vid_1_output.gif'

clipOne = (VideoFileClip(inputVideoPathOne).subclip((0.0),(10.0)).resize(0.2))
clipOne.write_gif(outputVideoPathOne,fps=15)

clipTwo = (VideoFileClip(inputVideoPathTwo).subclip((0.0),(10.0)).resize(0.2))
clipTwo.write_gif(outputVideoPathTwo,fps=15)