from gtts import gTTS
import csv
import requests
import re

def saveMM(row):
	tts = gTTS(row[4], lang = 'my')
	tts.save(f'build/tts/mm/{row[0]}.mp3')

def splitUnwanted(jpWord):
	if jpWord:
		if jpWord[0] == '（':
			jpWord = jpWord.split('）')[1]
		else:
			jpWord = jpWord.split('（')[0]
	return jpWord

def saveJP(row):
	kanji = splitUnwanted(row[3])
	kana = splitUnwanted(row[2])

	pattern = re.compile("^([ァ-ンー]+)+$")
	reResult = pattern.match(kana)
	languagepodUrl = f'https://assets.languagepod101.com/dictionary/japanese/audiomp3.php?kana={kana}'
	if reResult is None:
		languagepodUrl = f'https://assets.languagepod101.com/dictionary/japanese/audiomp3.php?kana={kana}&kanji={kanji}'

	response = requests.get(languagepodUrl)

	if response.headers["Content-length"] == "52288":
		tts = gTTS(kana, lang = 'ja')
		tts.save(f'build/tts/jp/{row[0]}.mp3')
	else:
		with open(f'build/tts/jp/{row[0]}.mp3', 'wb') as f:
		    f.write(response.content)

	print(f'languagepodUrl {response.headers["Content-length"]} {languagepodUrl}')


with open('Win Kotoba - TTS output.csv') as csvfile:
	reader = csv.reader(csvfile)
	for index, row in enumerate(reader):
		if index == 0: continue
		print(f'{row[0]}, {row[4]}, {row[2]}, {row[3]}')
		if row[4]: saveMM(row)
		if row[2]: saveJP(row)
		# if index == 10: break
