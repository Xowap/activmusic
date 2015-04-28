# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, HTML
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from activmusic.apps.uploadmgr.models import AudioMedia


class AudioMediaForm(forms.ModelForm):
    class Meta:
        model = AudioMedia
        fields = ['url']

    def __init__(self, owner, *args, **kwargs):
        super(AudioMediaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self._owner = owner
        self.setup_layout()

    def setup_layout(self):
        self.helper.layout = Layout(
            Fieldset(
                _('Media Info'),

                'url',
            ),

            HTML('<div class="row">'
                 '  <div class="col-sm-8 col-sm-offset-4">'
                 '      <button class="btn btn-primary" type="submit">{}</button>'
                 '  </div>'
                 '</div>'.format(ugettext('Upload')))

        )

        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-8'

    def save(self, commit=True):
        instance = super(AudioMediaForm, self).save(commit=False)

        instance.owner = self._owner

        if commit:
            instance.save()
            self.save_m2m()

        return instance
