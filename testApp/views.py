from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from testApp.forms import UserProfileForm
from testApp.models import Country,State,City
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
import json




class HomePage(TemplateView):
	def get(self,request):
		return render(request,'homepage.html')


	def post(self,request):

		return render(request,'homepage.html')





class Signup(TemplateView):

	def get(self,request):
		return render(request,'signup.html')


	def post(self,request):

		# data = User.objects.get('username')
		# print(data)

		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		email = request.POST.get('email')
		rawpassword= request.POST.get('rawPassword')
		confirmpasssword= request.POST.get('confirmPassword')
		phone = request.POST.get('phone')
		image = request.FILES.get('image')

		if firstname is None or lastname == "" or email=="" or rawpassword=='' or confirmpasssword=='' or phone == '':

			print('all fields are mandatory')
		else:
			if rawpassword == confirmpasssword:
				try:
					user = User.objects.get(email = email)
					print("user already exists")
				except:
					user = User(first_name = firstname ,last_name = lastname, username = email,email = email)
					user.set_password(confirmpasssword)
					user.save()
					profileData = UserProfile(userID = user,phoneNumber = phone,profilePic = image)
					profileData.save()
					
					return HttpResponseRedirect('login')
			else:
				print('password does not match...')
		return render(request,'signup.html')



class Login(TemplateView):
	template_name = 'login.html'

	def get(self,request):
		if request.user.is_authenticated:                                                     
			return HttpResponseRedirect("/")
		else:
			return render(request,self.template_name,{})

	def post(self, request, *args, **kwargs):
		email = request.POST.get('email')
		password = request.POST.get('password')
		try:
			user = User.objects.get(email=email)
			userauth = authenticate(username=user.username, password=password)
			if userauth:
				login(request, user,backend='django.contrib.auth.backends.ModelBackend')
				if request.user.is_authenticated:
					return HttpResponseRedirect('profile/'+str(user.id))
				else:
					return HttpResponseRedirect('login')
			else:
				return HttpResponseRedirect('login')
		except Exception as e:
			
			return HttpResponseRedirect('login')


class Profile(TemplateView):
	template_name = 'homepage.html'

	def get(self,request,*args, **kwargs):
		current_id = kwargs.get('user_id')#used to get id from the url 
		user_id = request.user.id #its in string format
		print(type(user_id),'uuuuuuuuuuu')
		print(type(current_id),'cccccccccc')

		if request.user.is_authenticated and int(user_id) == int(current_id):
			user_obj  = User.objects.get(id = current_id)
			#-----------------------------
			profileData = UserProfile.objects.get(userID = user_obj)

			return render(request,'profile.html',locals())
			
		else:
			# return render(request,self.template_name,{})
			return HttpResponseRedirect('/')
		
		return render(request,'profile.html')

	def post(self,request):
		return render(request,'profile.html')



class UserLogout(View):
	def get(self,request):
		logout(request)
		return HttpResponseRedirect('/')



# class ForgetPassword(TemplateView):
	
# 	def get(self,request):
# 		return render(request,'forgetPassword.html')

# 	def post(self,request):
        
# 		email = request.POST.get('email')
# 		userEmail = User.objects.get(username = email)
# 		if userEmail:

# 			newPassword = request.POST.get('newPassword')
# 			confirmPassword = request.POST.get('confirmPassword')
# 			if newPassword == confirmpasssword:
# 				pass

# 		return render(request,'login')



class EditProfile(TemplateView):

	def get(self,request):
		user_data = UserProfile.objects.get(userID=request.user)
		return render(request,'edit.html',locals())

	def post(self,request):
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		phone = request.POST.get('phone')
		image = request.FILES.get('image')

		user = User.objects.get(id = request.user.id)
		profileData = UserProfile.objects.get(userID = request.user)

		if firstname:
			user.first_name = firstname
		if lastname:
			user.last_name = lastname
		if phone:
			if len(phone) >= 10:
				profileData.phoneNumber = phone
			else:
				return HttpResponse('small length phone')
		if image:
			profileData.profilePic = image
	
		user.save()
		profileData.save()


		return HttpResponseRedirect('/')	


		# user = User(id = user_id ,first_name = firstname ,last_name = lastname)

		# user.set_password(password)
		# user.save(update_fields=["first_name","last_name"])
		# userProfileData = UserProfile(userID = user,phoneNumber = phone,profilePic = image)
		# userProfileData.save(update_fields=["phoneNumber","profilePic"])


class AllUsers(TemplateView):

	def get(self,request):

		if request.user.is_authenticated:

			profileData = UserProfile.objects.all()

			return render(request,'all_users_data.html',{'profileData': profileData})
		else:
			return render(request,'login.html')

	def post(self,request):
		return render(request,'all_users_data.html')




class DeleteData(View):
	def get(self,request):

	    # user = kwargs.get('user_id')
	    user = request.GET.get('user_id')
	   
	    print(user,"6465555555555555555555555555555555555")
	    data = User.objects.get(id = int(user))
	    # print(data.userID)
	    data.delete()
	    return HttpResponseRedirect("allusers")

	
class AdminEdit(TemplateView):
	
	def get(self,request):

		url_id = request.GET.get('user_id')

		user_obj = UserProfile.objects.get(userID = url_id)

		return render(request,'adminedit.html',locals())

	def post(self,request):
		if request.user.is_authenticated:

			firstname = request.POST.get('firstname')
			lastname = request.POST.get('lastname')
			phone = request.POST.get('phone')
			image = request.FILES.get('image')

			url_id = request.GET.get('user_id')

			user = User.objects.get(id = url_id)
			profileData = UserProfile.objects.get(userID = user)

			if firstname:
				user.first_name = firstname
			if lastname:
				user.last_name = lastname
			if phone:
				profileData.phoneNumber = phone
			if image:
				profileData.profilePic = image
		
			user.save()
			profileData.save()

			return HttpResponseRedirect('allusers')

		else:
			return HttpRespose('you are not authenticated user')




# class GetJsonData(TemplateView):

# 	HttpResponse(content_type/json)



class WorldData(TemplateView):

	def get(self,request):

		country_data = Country.objects.all()
		# state_data = State.objects.all()
		city_data = City.objects.all()
		return render(request,'worlddata.html',locals())
	def post(self,request):
		return render(request,'worlddata.html')

class Dropdown(View):
	 
	 def get(self,request):
	 	return render(request,'dropdown.html')

class GetStateFromCountry(View):

	def get(self,request):
		
		response={}
		state_list = []
		try:
			
			country_id = request.GET.get('id',None)
			print(country_id,'---------------------------------------------')

			if country_id:
				county_obj = Country.objects.get(id=country_id)
				states_data = State.objects.filter(countryID=county_obj)

				
				for i in states_data:

					state_list.append({'state_id':i.id,'state_name':i.state})


				print(state_list,'--------listtttt-----------------------------')

			# for i ,j in dict(state_list).items():
			#     if(isinstance(j, list)):
			#     	for k in j:
			#     		print(k,'----------------value........................')
			for i in state_list:
				print(i,'-----------------iiiiiiiiii-------------')

			response['status']=True
			response['data']=state_list


			# state_list.extend('helo','world')


			# state_list.append('state
			

			# return response(request,'worlddata.html',{'state_data':states_data})
			# response['states_data']=state_list

		except Country.DoesNotExist:
			response['status']=False
			response['error']="No data found"

		except Exception as e:
			raise e
			response['status']=False
			response['error']=str(e)

		
	
		return HttpResponse(json.dumps(response), content_type="application/json")



class GetCityFromState(View):

	def get(self,request):
		
		response={}
		city_list = []
		try:
			
			state_id = request.GET.get('id',None)
			print(state_id,'---------------------------------------------')

			if state_id:
				state_obj = States.objects.get(id=state_id)
				city_data = City.objects.filter(stateID=state_obj)

				
				for i in city_data:

					city_list.append({'city_id':i.id,'city_name':i.city})


				print(city_list,'--------listtttt-----------------------------')

			# for i ,j in dict(state_list).items():
			#     if(isinstance(j, list)):
			#     	for k in j:
			#     		print(k,'----------------value........................')
			for i in city_list:
				print(i,'-----------------iiiiiiiiii-------------')

			response['status']=True
			response['data']=city_list


			# state_list.extend('helo','world')


			# state_list.append('state
			

			# return response(request,'worlddata.html',{'state_data':states_data})
			# response['states_data']=state_list

		except State.DoesNotExist:
			response['status']=False
			response['error']="No data found"

		except Exception as e:
			raise e
			response['status']=False
			response['error']=str(e)

		
	
		return HttpResponse(json.dumps(response), content_type="application/json")



