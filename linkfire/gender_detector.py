import requests
from base import Base

api_base = "https://innovaapi.aminer.cn/tools/"
api_version = "v1"

def get_gender(name):
	'''
	Returns the gender of a given name.

			Parameters:
					name (str): A person name
					
			Returns:
					'male' or 'female'
	'''
	name = name.replace(" ", "+")
	url = f"{api_base}{api_version}/predict/gender?name={name}&org=Tsinghua"
	resp = requests.get(url)
	return resp.json()['data']['Final']['gender']


# if __name__ == '__main__':
# 	print(get_gender("valeria vasquez xd"))


class GenderUpdater(Base):

	def get_actors_without_gender(self):
		sql = "SELECT id, name FROM actor_dim WHERE gender = 0"
		self.cursor.execute(sql)
		return self.cursor.fetchall()
		
	def update_gender(self):
		for actor in self.get_actors_without_gender():
			if actor[1]:
				try:
					gender = get_gender(actor[1])
				except Exception as e:
					print(f'API error:"{e}" - actor_id:"{actor[0]}"')
					continue
				
				print(f"==name={actor[1]}, gender={gender}, id={actor[0]}")
				if gender == 'male':
					val = 1
				elif gender == 'female':
					val = 2
				elif gender == 'UNKNOWN':
					val = 3
	
				sql = "UPDATE actor_dim SET gender = %s WHERE id = %s"
				self.cursor.execute(sql, (val, actor[0],))
				self.db.commit()
	
if __name__ == '__main__':
	gu = GenderUpdater()
	gu.update_gender()
