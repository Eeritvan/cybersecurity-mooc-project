from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Note

@login_required
def addNote(request):
	user = User.objects.filter(username = request.user)[0]
	if request.method == 'POST':
		text = request.POST.get('text')
		if text:
			Note.objects.create(content=text, owner=user)
	return redirect('/')

@login_required
def homePageView(request):
	user = User.objects.filter(username = request.user)[0]
	search_query = request.GET.get('search', '')

	# Vulnerability: SQL Injection
	# ---
	# You can test flaw this by inserting: %' UNION SELECT id, username || " " || password as content FROM auth_user --
	# to the search field. This example input should expose other users' usernames and password hashes

	# FIX:
	# removing/commenting out the if-statement below and replacing it with the following:
	# notes = Note.objects.filter(owner=user.id, content__icontains=search_query)

	if search_query:
		query = f"""
			SELECT id, content FROM pages_note
			WHERE owner_id = {user.id} AND content LIKE '%{search_query}%'
		"""
		notes = Note.objects.raw(query)
	else:
		notes = Note.objects.filter(owner=user.id)

	context = {'notes': notes, 'userID': user.id}
	return render(request, 'pages/index.html', context=context)

def userData(request, id):
	try:
		# Vulnerability: Broken Access Control
		# ---
		# You can access other users' personal information by changing id in the url /user/(id)
		# You can view it access even logging in. You try this by visiting for example
		# http://127.0.0.1:8000/user/1/ and changing the id number to 2

		# FIX: 
		# Checking if current user is the one visiting profile. Simple if-statement will do the trick.
		#if request.user.id != id:
		#	return HttpResponse("no data found")
		
		user = User.objects.filter(id = id)[0]

		notes = Note.objects.filter(owner = user.id)
		jsonNotes = [{'id': f.id, 'content': f.content, 'owner': f.owner.username} for f in notes]

		data = {
			'id': user.id,
			'email': user.email,
			'username': user.username,
			'first_name': user.first_name,
			'last_name': user.last_name,
			'is_superuser': user.is_superuser,
			'is_staff': user.is_staff,
			'is_active': user.is_active,
			'date_joined': user.date_joined,
			'last_login': user.last_login,
			'notes': jsonNotes
		}

		return JsonResponse(data)
	except:
		return HttpResponse("no data found")