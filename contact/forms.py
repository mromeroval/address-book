from django import forms
from .models import Users
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button, HTML
from crispy_forms.bootstrap import FormActions


class ContactForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=25)
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)   
    position = forms.CharField(label='Position', max_length=50, required=False)
    department = forms.CharField(label='Office/Department', max_length=255, required=False)
    executive = forms.BooleanField(required=False)
    executive_assistant = forms.BooleanField(required=False)
    phone = forms.CharField(label='Phone Number', max_length=25, required=True)
    email = forms.CharField(label='E-mail', max_length=50, required=True)
    supports = forms.CharField(label='Supports', max_length=100, required=False)
    supported_by = forms.CharField(label='Supported By', max_length=100, required=False)
    space_available = forms.CharField(label='Space Available', max_length=255, required=False)
    notes = forms.CharField(label='Notes', max_length=500, required=False, widget=forms.Textarea)
    office_location = forms.CharField(label='Office Location', max_length=255, required=False)
    active = forms.BooleanField(initial = 1,required=False)
    admin = forms.BooleanField(required=False)
    
    class Meta:
        model = Users
        fields = [
                  "username",
                  "first_name",
                  "last_name",
                  "phone",
                  "email",                  
                  "position",
                  "department",                         
                  "office_location",
                  "supports",
                  "supported_by",
                  "space_available",
                  "notes",                  
                  "executive",
                  "executive_assistant",
                  "active",
                  "admin"
                  ]
    def __init__(self, *args, **kwargs):
      super(ContactForm, self).__init__(*args, **kwargs)
      self.helper = FormHelper()
      self.helper.layout = Layout(
            Fieldset(
                "",
                "username",
                "first_name",
                "last_name",
                "phone",
                "email",
                "position",
                "department",
                "office_location",
                "supports",
                "supported_by",
                "space_available",
                "notes",
                "executive",
                "executive_assistant",
                "active",
                "admin"
            ),
            FormActions(
              Submit('save', 'Save', css_class='btn btn-sm btn-dark'),

              HTML("""<a role="button" class="btn btn-sm btn-dark"
    href="{% url "index" %}">Cancel</a>""")
            )
        )
        
class SearchContactForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name :&nbsp;', max_length=25, required=False)
    last_name = forms.CharField(label='Last Name :&nbsp;', max_length=25, required=False) 
    
    class Meta:
        model = Users
        fields = [
                  "first_name",
                  "last_name",
                  ]
    def __init__(self, *args, **kwargs):
      super(SearchContactForm, self).__init__(*args, **kwargs)
      self.helper = FormHelper()
      self.helper.layout = Layout(
            Fieldset(
                '',
                'first_name',
                'last_name',
            ),
            ButtonHolder(
                Submit('submit', 'Search', css_class='btn btn-sm btn-dark')
            )
        )

class SearchDepartmentForm(forms.ModelForm):  
    department = forms.CharField(label='Department :&nbsp;', max_length=30, required=False)
    
    class Meta:
        model = Users
        fields = ["department"]

    def __init__(self, *args, **kwargs):
      super(SearchDepartmentForm, self).__init__(*args, **kwargs)
      self.helper = FormHelper()
      self.helper.layout = Layout(
            Fieldset(
                '',
                'department',
            ),
            ButtonHolder(
                Submit('submit', 'Search', css_class='btn btn-sm btn-dark')
            )
        )        
        
class SearchPositionForm(forms.ModelForm):
    position = forms.CharField(label='Position :&nbsp;', max_length=30, required=False)

    class Meta:
        model = Users
        fields = ["position"]
    def __init__(self, *args, **kwargs):
      super(SearchPositionForm, self).__init__(*args, **kwargs)
      self.helper = FormHelper()
      self.helper.layout = Layout(
            Fieldset(
                '',
                "position"
            ),
            ButtonHolder(
                Submit('submit', 'Search', css_class='btn btn-sm btn-dark')
            )
        )