import webbrowser

class Movie():
	def __init__ (self, title, storyline, poster_image_url, trailer_youtube_url):
		""" 
		Purpose: Organize movie data
		Inputs: title, storyline, poster image and trailer
		"""
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer (self):
		""" 
		Input: Itself
		Output: Opens the movie trailer
		"""
		webbrowser.open(self.trailer_youtube_url)
