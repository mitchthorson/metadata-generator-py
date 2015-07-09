class Generator(object):
    def __init__(self):
        self.get_title()
        self.get_description()
        self.get_image()
        self.get_url()
        self.create_meta()
        self.output_meta()

    def get_description(self):
        self.description = raw_input("Description: ")

    def get_title(self):
        self.title = raw_input("Title: ")

    def get_image(self):
        self.image = raw_input("Image (url): ")

    def get_url(self):
        self.url = raw_input("Page URL: ")

    output_template = '<meta name="description" content="%(description)s" /> \n <meta property="og:description" content="%(description)s"/> \n <meta name="twitter:description" content="%(description)s"> \n <meta property="og:type" content="website"> \n <meta name="twitter:title" content="%(title)s"> \n <meta property="og:title" content="%(title)s"/> \n <meta name="twitter:card" content="summary_large_image"> \n <meta name="twitter:url" content="%(url)s"> \n <meta property="og:image" content="%(image)s"> \n <meta name="twitter:image" content="%(image)s">'

    def create_meta(self):
        self.meta = self.output_template % {"description": self.description, "url": self.url, "title": self.title, "image": self.image}

    def output_meta(self):
        print ("Your new meta data: \n \n \n %s \n \n \n" % self.meta)
