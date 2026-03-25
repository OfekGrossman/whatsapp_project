"""
Forms for the messaging application.

This module contains form classes for user registration and message creation.
It extends Django's built-in forms and implements custom validation for messages
with length restrictions and user input validation.

Classes:
    RegistrationForm: Form for new user registration
    MessageForm: Form for creating new messages with content length validation (max 1024 chars)
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Message

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content']
