from django import forms

class UploadFile(forms.Form):
    file = forms.FileField()

class UploadListIds(forms.Form):

	TYPES = (('pdb', 'PDB'), ('uniprotkb', 'UniProtKB'))

	ids_type = forms.ChoiceField(widget=forms.RadioSelect, choices=TYPES, initial='pdb')
	ids = forms.CharField(widget=forms.Textarea(
		attrs={'class':'form-control', 'placeholder':'Paste here the list of ids'}))
