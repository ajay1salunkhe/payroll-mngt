from django.forms import ModelForm
from django import forms
from .models import Attendance

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = (
            'employee',
            'work_type',
            'date',
            'mark',
            'rem_privilege_leave',
            'rem_casual_leave',
            'leave_type'
        )
    
