from django import forms
from .models import ContactMessage, Enquiry, PaymentRecord


class BootstrapMixin:
    def apply_bootstrap(self):
        for _, field in self.fields.items():
            widget = field.widget
            if isinstance(widget, forms.RadioSelect):
                widget.attrs.update({'class': 'form-check-input'})
            elif isinstance(widget, forms.CheckboxInput):
                widget.attrs.update({'class': 'form-check-input'})
            elif isinstance(widget, forms.CheckboxSelectMultiple):
                widget.attrs.update({'class': 'form-check-input'})
            else:
                existing = widget.attrs.get('class', '')
                widget.attrs['class'] = f"{existing} form-control".strip()


class ContactForm(forms.ModelForm, BootstrapMixin):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'subject': forms.Select(choices=[
                ('Admissions', 'Admissions'),
                ('Transport', 'Transport'),
                ('Academics', 'Academics'),
                ('Fees', 'Fees'),
                ('General Enquiry', 'General Enquiry'),
            ]),
            'message': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {'name': 'Full Name'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()


class PaymentForm(forms.ModelForm, BootstrapMixin):
    PAYMENT_METHOD_CHOICES = [
        ('Card', 'Credit/Debit Card'),
        ('UPI', 'UPI'),
        ('NetBanking', 'Net Banking'),
        ('BankTransfer', 'Bank Transfer'),
    ]
    amount = forms.DecimalField(min_value=500, decimal_places=2, max_digits=10)
    payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect)
    card_number = forms.CharField(required=False)
    card_holder = forms.CharField(required=False)
    card_expiry = forms.CharField(required=False)
    card_cvv = forms.CharField(required=False)
    upi_id = forms.CharField(required=False)

    class Meta:
        model = PaymentRecord
        fields = ['student_name', 'roll_number', 'class_section', 'fee_type', 'amount', 'payment_method']
        widgets = {
            'class_section': forms.Select(choices=[
                ('Nursery - A', 'Nursery - A'),
                ('Class 2 - B', 'Class 2 - B'),
                ('Class 5 - A', 'Class 5 - A'),
                ('Class 8 - C', 'Class 8 - C'),
                ('Class 10 - A', 'Class 10 - A'),
                ('Class 12 - Commerce', 'Class 12 - Commerce'),
            ]),
            'fee_type': forms.Select(choices=PaymentRecord.FEE_TYPE_CHOICES),
        }
        labels = {
            'student_name': 'Student Name',
            'roll_number': 'Roll Number / Admission Number',
            'class_section': 'Class & Section',
            'fee_type': 'Fee Type',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()
        self.fields['card_number'].widget.attrs.update({'placeholder': '1234 5678 9012 3456'})
        self.fields['card_holder'].widget.attrs.update({'placeholder': 'Card Holder Name'})
        self.fields['card_expiry'].widget.attrs.update({'placeholder': 'MM/YY'})
        self.fields['card_cvv'].widget.attrs.update({'placeholder': 'CVV'})
        self.fields['upi_id'].widget.attrs.update({'placeholder': 'name@upi'})

    def clean(self):
        cleaned_data = super().clean()
        payment_method = cleaned_data.get('payment_method')
        if payment_method == 'Card':
            for field in ['card_number', 'card_holder', 'card_expiry', 'card_cvv']:
                if not cleaned_data.get(field):
                    self.add_error(field, 'This field is required for card payment.')
        if payment_method == 'UPI' and not cleaned_data.get('upi_id'):
            self.add_error('upi_id', 'Please enter a valid UPI ID.')
        return cleaned_data


class EnquiryForm(forms.ModelForm, BootstrapMixin):
    DOCUMENT_CHOICES = [
        ('Birth Certificate', 'Birth Certificate'),
        ('Aadhaar', 'Aadhaar'),
        ('Transfer Certificate', 'Transfer Certificate'),
        ('Passport Photo', 'Passport Photo'),
    ]
    documents = forms.MultipleChoiceField(choices=DOCUMENT_CHOICES, widget=forms.CheckboxSelectMultiple)
    declaration = forms.BooleanField(required=True)

    class Meta:
        model = Enquiry
        fields = [
            'student_name', 'dob', 'gender', 'nationality', 'applying_class', 'medium',
            'father_name', 'mother_name', 'occupation', 'income', 'contact', 'email', 'address',
            'documents', 'referral_source', 'preferred_session', 'special_requirements', 'declaration'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]),
            'applying_class': forms.Select(choices=[
                ('Nursery', 'Nursery'), ('KG', 'KG'), ('Class 1', 'Class 1'),
                ('Class 5', 'Class 5'), ('Class 8', 'Class 8'),
                ('Class 10', 'Class 10'), ('Class 11', 'Class 11')
            ]),
            'medium': forms.Select(choices=[('English', 'English'), ('Bilingual', 'Bilingual')]),
            'referral_source': forms.Select(choices=[
                ('Google Search', 'Google Search'),
                ('Social Media', 'Social Media'),
                ('Parent Referral', 'Parent Referral'),
                ('School Event', 'School Event'),
                ('Advertisement', 'Advertisement')
            ]),
            'preferred_session': forms.Select(choices=[('2024-25', '2024-25'), ('2025-26', '2025-26')]),
            'special_requirements': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'student_name': 'Student Name',
            'dob': 'Date of Birth',
            'contact': 'Contact Number',
            'occupation': 'Parent/Guardian Occupation',
            'income': 'Annual Family Income',
            'special_requirements': 'Message / Special Requirements',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap()

    def clean_documents(self):
        documents = self.cleaned_data['documents']
        if not documents:
            raise forms.ValidationError('Please select at least one document.')
        return documents
