from app import app
from forms import testForm
from flask import render_template, request, redirect
# from app.forms import


@app.route('/', methods=['GET', 'POST'])
def index():
	update = 'True'
	if request.method == 'POST':
		update = 'True'
		print "posted"
	form = testForm(request.form, csrf_enabled=True)
	return render_template("index.html", form=form, update=update)