from django.urls import path

from .views import show_main, show_experience, show_projects, create_project, get_projects_json, delete_project, update_project, register, login_user, logout_user, toggle_star, create_project_ajax, add_project_ajax, contact_list, contact_add, contact_delete, contact_search, contact_edit, contact_row, contact_update

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("projects/edit/<uuid:project_id>/", update_project, name="update_project"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("projects/add-ajax/", add_project_ajax, name="add_project_ajax"),
    path("", contact_list, name="contact_list"),
    path("contacts/add/", contact_add, name="contact_add"),
    path("contacts/<int:pk>/delete/", contact_delete, name="contact_delete"),
    path("contacts/search/", contact_search, name="contact_search"),
    path("contacts/<int:pk>/edit/", contact_edit, name="contact_edit"),
    path("contacts/<int:pk>/row/", contact_row, name="contact_row"),
    path("contacts/<int:pk>/update/", contact_update, name="contact_update"),
]