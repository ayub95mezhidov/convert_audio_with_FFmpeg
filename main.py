import ffmpeg

input_file = 'input_file.mp3'
output_file = 'output_file.wav'

stream = ffmpeg.input(input_file)
audio = stream.audio
audio = ffmpeg.output(audio, output_file)

ffmpeg.run(audio)
