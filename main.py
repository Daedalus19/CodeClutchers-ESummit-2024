'''
Main Code runner
'''

import transcribe
import summarizer

vid_link = input("Enter the vid link : ")
transcribe.yt_download(vid=vid_link)
transcript = transcribe.transcribe()
transcribe.write_file(text=transcript)

summarizer.summary()