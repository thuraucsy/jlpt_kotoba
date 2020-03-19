from gtts import gTTS
import csv

def saveToFile(row):
	tts = gTTS(row[1], lang = 'my')
	tts.save(f'build/tts/mm/{row[0]}.mp3')

with open('ttsMyanmar.csv') as csvfile:
	reader = csv.reader(csvfile)
	for index, row in enumerate(reader):
		if index == 10: break
		print(','.join(row))
		saveToFile(row)