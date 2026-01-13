from django import forms
from .models import DoramaNews, DoramaVideo  # Импортируем обе модели
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# --- Форма для добавления Новостей ---
class DoramaNewsForm(forms.ModelForm):
    class Meta:
        model = DoramaNews
        fields = ['title', 'dorama_name', 'description', 'image']
        labels = {
            'title': 'Заголовок новости',
            'dorama_name': 'Название дорамы',
            'description': 'Описание',
            'image': 'Изображение',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'dorama_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название дорамы'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Описание новости'}),
        }

# --- Форма для регистрации Пользователей ---
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Электронная почта")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

# --- Форма для добавления Видео (Reels) ---
class DoramaVideoForm(forms.ModelForm):
    class Meta:
        model = DoramaVideo
        fields = ['title', 'video_file', 'video_url']
        labels = {
            'title': 'Название видео',
            'video_file': 'Файл видео (MP4)',
            'video_url': 'Ссылка на YouTube/VK',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название видео'}),
            'video_file': forms.FileInput(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Ссылка (если нет файла)'}),
        }