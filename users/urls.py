from django.urls import path
from .views import SignupView, ProfileView, UpdateProfileView, AddRemoveSavedView, SavedView

app_name = 'users'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/<str:username>', ProfileView.as_view(), name='profile'),
    path('update/', UpdateProfileView.as_view(), name='update'),
    path('addremovesaved/<int:product_id>', AddRemoveSavedView.as_view(), name='addremovesaved'),
    path('saveds', SavedView.as_view(), name='saveds'),

]

