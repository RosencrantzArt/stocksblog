from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def clean_text(self):
        text = self.cleaned_data.get('text', '').strip()

        if not text:
            raise forms.ValidationError("Comment cannot be empty or only spaces.")
        
        if len(text) > 1000:
            raise forms.ValidationError("Comment cannot exceed 1000 characters.")

        
        forbidden_words = ['spam', 'offensiveword']
        for word in forbidden_words:
            if word in text.lower():
                raise forms.ValidationError("Inappropriate language detected.")
        
        return text