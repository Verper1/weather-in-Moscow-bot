import os
import time
from datetime import datetime
import schedule
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests
from decryption import moon_phase_dict
import telebot
from dotenv import find_dotenv, load_dotenv
import threading
