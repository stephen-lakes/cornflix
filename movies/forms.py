from django import forms

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=50, label='')
    
    search_term.widget.attrs.update({'class': 'search', 'placeholder': 'Search for a movie'})

