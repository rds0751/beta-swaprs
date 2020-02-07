from django import forms

from crispy_forms import (bootstrap,
                          layout)
from crispy_forms.helper import FormHelper

from leaflet.forms.widgets import LeafletWidget

from apps.board.models import Post

# Post Input
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'unit_type', 'location', 'category', 'image1', 'image2', 'image3']
        widgets = {}

    # Appearance of the Form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'my_class'
        self.fields['body'].widget.attrs['class'] = 'my_class'
        self.fields['unit_type'].widget.attrs['class'] = 'my_class'
        self.fields['location'].widget.attrs['class'] = 'my_class'
        self.fields['category'].widget.attrs['class'] = 'my_class'
        self.fields['image1'].widget.attrs['class'] = 'my_class'
        self.fields['image2'].widget.attrs['class'] = 'my_class'
        self.fields['image3'].widget.attrs['class'] = 'my_class'
        

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'unit_type', 'location', 'category']
        widgets = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # TODO: Don't repeat from the PostForm
        self.helper = FormHelper(self)
        self.helper.layout = layout.Layout(
            layout.Fieldset(
                '',
                layout.Field('title', placeholder='A snappy title'),
                'body',
                'tags',
                bootstrap.PrependedText('price', '$'),
                'unit'
            ),
            bootstrap.FormActions(
                layout.Submit('submit', 'Update post', css_class='btn btn-success'),
                layout.HTML('<a class="btn btn-outline-secondary" href="{% url "board:detail" slug=object.slug %}">Cancel</a>'),
            )
        )
        self.helper.form_tag = False
