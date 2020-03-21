import re
import os
import bz2
import wget
from datetime import datetime
import time

pulldelay = 3600

urls = ['https://apps.foldingathome.org/daily_user_summary.txt.bz2', 
'https://apps.foldingathome.org/daily_team_summary.txt.bz2']

path = os.getcwd() + '/files/'

try:
	while True:
		now = datetime.now()
		print('Downloading team and user stat flat files...')
		for url in urls:
			filename = path + url.split('/')[3]
			print('Checking if file exists...')
			print(filename)


			if os.path.exists(filename):
				print("Deleting old flat file...")
				os.remove(filename)
			else:
				print("The file does not exist...")

			print('Downloading file...')
			wget.download(url, filename)

			print()

		file0 = path + '/daily_team_summary.txt.bz2'
		file1 = path + '/daily_user_summary.txt.bz2'

		teamfile = bz2.open(file0, "rt")
		userfile = bz2.open(file1, "rt")

		teams = teamfile.readlines()
		users = userfile.readlines()

		teamid = '244098'

		print()
		print("Pull datetime: ", now)
		print()

		print('=================================================')
		print('          MID SOUTH DYNAMICS TEAM STATS')
		print('=================================================')

		for team in teams:
			try:
				teaminfo = re.split('\t+', team.rstrip('\t\n'))
				if teamid == teaminfo[0]:
					print('   team id: ' + teaminfo[0])
					print('   team name: ' + teaminfo[1])
					print('   score: ' + teaminfo[2])
					print('   work units: ' + teaminfo[3])
			except IndexError:
				pass

		print()

		print('================================')
		print('          USER STATS')
		print('================================')

		for user in users:
			try:
				userinfo = re.split('\t+', user.rstrip('\t\n'))
				if teamid == userinfo[3]:
					print('   username: ' + userinfo[0])
					print('   credit: ' + userinfo[1])
					print('   work units: ' + userinfo[2])
					print('--------------------------------')
			except IndexError:
				pass

		print()
		print('Next update in 1 hour...')
		print()
		print('Press CTRL+C to exit script...')
		print()
		time.sleep(pulldelay)

except KeyboardInterrupt:
	pass

print()
print('Script has exited...')
print()

		

