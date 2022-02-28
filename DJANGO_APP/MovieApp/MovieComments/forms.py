from django import forms
from .models import Movie


class AddNewComment(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie', 'comment']

    movie = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))
    comment = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['movie'].choices = Movie.objects.all().values_list("movie","movie").distinct()



class ChooseMovie(forms.Form):
    movie = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['movie'].choices = Movie.objects.all().values_list("movie","movie").distinct()