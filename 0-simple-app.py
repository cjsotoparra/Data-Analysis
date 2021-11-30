import justpy as jp

#Create simple webpage
def app():

	#create
	wp = jp.QuasarPage()

	#create 2 elements and add them to our component
	h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
	p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
	return wp

#call app function
jp.justpy(app)
