# from .models import Profile
# from django import forms
# from crispy_bootstrap5.bootstrap5 import FloatingField, BS5Accordion
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout
# from crispy_forms.bootstrap import AccordionGroup


# class ProfileForm(forms.ModelForm):
    
#     helper = FormHelper()
#     helper.layout = Layout(
#         # self.helper.form_tag = False
#         # self.helper.include_media = False 
#         BS5Accordion(
#             AccordionGroup('#1',  
#                 FloatingField("last_name", autocomplete="last_name"),
#                 FloatingField("first_name", autocomplete="first_name"),
#                 'user_pic'
#             ),
#             AccordionGroup('#2',
#                 'bio',
#             ),
#             AccordionGroup('#3',
#                 FloatingField("location", autocomplete="location"),
#                 FloatingField("website", autocomplete="website"),
#                 FloatingField("phone", autocomplete="phone"),
#                 FloatingField("birth_date", autocomplete="birth_date"),
                
#             ),
#             flush=True,
#             # always_open=True
#         )
#     )
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
        
#     class Meta:
#         model = Profile
#         fields = ['bio','last_name','first_name','location','website','phone','user_pic',"birth_date"]
#         widgets = {}