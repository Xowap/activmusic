# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# activmusic
# (c) 2014 ActivKonnect

AUTH_USER_MODEL = 'register.User'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_FORM_CLASS = 'activmusic.apps.register.forms.UserSignupForm'
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = False
ACCOUNT_ADAPTER = 'activmusic.apps.register.allauth_adapter.AccountAdapter'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[activmusic]'

SOCIALACCOUNT_ADAPTER = 'activmusic.apps.register.allauth_adapter.SocialAccountAdapter'
