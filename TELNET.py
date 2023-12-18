"""
TELNET ID V3
UNIQUE ID
BY SOLARIS SOFTWARE BULARES 🌞

28/10/2023
"""

from hashlib import sha3_512
from collect_info import*
import os


def hash(src):
	return sha3_512(src.encode()).hexdigest().upper()


def get_user_ID(geo, user_entry):

	gl = ""
	if geo is True:
		gl = geolocalisation()

	gmi = get_more_info()

	os.remove("result.txt")
	os.remove("network.txt")

	UID = user_entry+gl+gmi

	return hash(UID)

