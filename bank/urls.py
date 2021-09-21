
from django.urls import path
from . import views

urlpatterns = [
   path("", views.HomePage, name="Home"),
   path("withdraw/<int:id>/", views.WithdrawPage, name="Withdraw"),
   path("deposit/<int:id>/", views.DepositPage, name="Deposit"),
   path("history/", views.HistoryPage, name="History"), 
   path("transfer/<int:id>/", views.TransferPage, name="Transfer"),
   path("users/", views.UsersPage, name="Users"),

]