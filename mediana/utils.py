import csv
import configparser
from dataclasses import dataclass


@dataclass
class DbConfig:
	host: str
	password: str
	user: str
	database: str
	port: int

@dataclass
class Site:
	debug: bool

@dataclass
class Config:
	site: Site
	db: DbConfig

def load_config(path: str = 'site.ini'):
	config = configparser.ConfigParser()
	config.read(path)
	site = config["site"]
	return Config(
		site=Site(debug=site['debug']), 
		db=DbConfig(**config["db"]),
	)

def get_file_path():
	config = load_config()
	# if config.site.debug == '':
	# 	return "D://Projects/projects/mediana_project"
	# else:
	return f"/root"

def write_users_to_csv(queryset):
	file_path = get_file_path()
	with open(f'{file_path}/users.csv', mode='w', newline='') as csv_file:
		writer = csv.DictWriter(csv_file, fieldnames=['ID'])
		# writer.writeheader()
		for obj in queryset:
			writer.writerow({'ID': str(obj.user_id)})
