# from django.conf.urls import url
from django.urls import path


from . import views



app_name = 'testApp'

urlpatterns = [

	# url(r'^test/$',views.first,name = 'test'),
	path('',views.HomePage.as_view(),name = 'home'),
	path('signup',views.Signup.as_view(),name = 'signup'),
	path('login',views.Login.as_view(), name = 'login'),
	path('profile/<user_id>',views.Profile.as_view(),name = 'profile'),
	path('logout',views.UserLogout.as_view(), name = 'logout'),
	path('edit',views.EditProfile.as_view(), name = 'edit'),
	path('allusers',views.AllUsers.as_view(),name = 'allusers'),
	path('deletedata',views.DeleteData.as_view(), name = 'deletedata'),
	path('adminedit',views.AdminEdit.as_view(),name = 'adminedit'),
	path('worlddata',views.WorldData.as_view(),name = 'worlddata'),

	path('dropdown',views.Dropdown.as_view(),name = 'dropdown'),
	path('getjsondata',views.GetStateFromCountry.as_view(),name = 'getjsondata'),
	path('getjsoncity',views.GetCityFromState.as_view(),name = 'getjsoncity'),





	# path('forgetPassword',views.ForgetPassword.as_view(),name = 'forgetPassword'),



]
