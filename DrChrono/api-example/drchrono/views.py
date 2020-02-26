from django.shortcuts import redirect
from django.views.generic import TemplateView
from social_django.models import UserSocialAuth
from datetime import datetime, date
from django.views.generic.edit import FormView
from forms import PatientCheckInForm, PatientUpdateProfileForm
from django.core.urlresolvers import reverse
from drchrono.endpoints import DoctorEndpoint, PatientEndpoint, AppointmentEndpoint
from . import utility
from django.shortcuts import HttpResponseRedirect


class SetupView(TemplateView):
    """
    The beginning of the OAuth sign-in flow. Logs a user into the kiosk, and saves the token.
    """
    template_name = 'kiosk_setup.html'


class DoctorWelcome(TemplateView):
    """
    The doctor can see what appointments they have today.
    """
    template_name = 'doctor_welcome.html'

    def make_api_request(self):
        """
        Use the token we have stored in the DB to make an API request and get doctor details. If this succeeds, we've
        proved that the OAuth setup is working
        """
        # We can create an instance of an endpoint resource class, and use it to fetch details
        access_token = utility.get_token()
        api = DoctorEndpoint(access_token)
        # Grab the first doctor from the list; normally this would be the whole practice group, but your hackathon
        # account probably only has one doctor in it.

        # u'date_of_last_appointment': u'2020-02-14' gives todays appnt
        return next(api.list())

    # def get_appointments_on_date(self,on_date):
    #     """ get patients data for this doctor"""
    #     access_token = utility.get_token()
    #     patients_api = PatientEndpoint(access_token)
    #     todays_appnt = []
    #
    #     patients_list = patients_api.list()
    #     for patient in patients_list:
    #         # print('\npatient = {}'.format(patient))
    #         last_appnt = patient.get('date_of_last_appointment', None)
    #         if last_appnt is not None and last_appnt != '':
    #             if datetime.strptime(last_appnt, '%Y-%M-%d') == on_date:
    #                 todays_appnt.append(patient)
    #
    #     return todays_appnt

    def get_appointments_on_date(self, on_date):
        access_token = utility.get_token()
        appnt_api = AppointmentEndpoint(access_token)
        return appnt_api.list(date=on_date)

    def get_context_data(self, **kwargs):
        print('get_context_data')
        kwargs = super(DoctorWelcome, self).get_context_data(**kwargs)
        # Hit the API using one of the endpoints just to prove that we can
        # If this works, then your oAuth setup is working correctly.
        # todays_date = datetime.strptime('2020-02-14', '%Y-%M-%d')
        todays_date = date.today()
        doctor_details = self.make_api_request()
        appointments_list = list(self.get_appointments_on_date(on_date=todays_date))
        kwargs['doctor'] = doctor_details
        kwargs['appointments'] = appointments_list

        print('appointments_list = {}'.format(appointments_list))
        return kwargs


class PatientCheckIn(FormView):
    print('PatientCheckIn')
    template_name = 'patient_check_in.html'
    form_class = PatientCheckInForm
    success_url = '/patient_update_profile/'
    patient_id = None

    def form_valid(self, form):
        print('form valid ssn=', form.cleaned_data['ssn'])
        try:
            # check if credenntials match a patient in the db
            access_token = utility.get_token()
            patient_api = PatientEndpoint(access_token)
            patient_list = list(
                patient_api.list(
                    {
                        'first_name': str(form.cleaned_data['first_name']),
                        'last_name': str(form.cleaned_data['last_name']),
                        'social_security_number': form.cleaned_data['ssn']
                    }
                )
            )
            self.patient_id = patient_list[0]['id']
            print('patient_list = ', patient_list)
            # send next(patient) to success_url
            return super(PatientCheckIn, self).form_valid(form)
        except Exception as e:
            print(e.message)
            return HttpResponseRedirect(reverse('patient_check_in'))

    def get_success_url(self):
        """ pass patient_id as a para to the success url """
        return reverse('patient_update_profile', kwargs={'patient_id': self.patient_id})


class PatientUpdateProfile(FormView):
    """
        view that lets patients update their profile and save it
    """
    template_name = 'patient_update_profile.html'
    form_class = PatientUpdateProfileForm
    success_url = '/patient_update_profile/'

    def get_context_data(self, **kwargs):
        """
        :return: dictionary to populate template data
        """
        print('PatientUpdateProfile get_context_data')
        print('self = ', self)
        print('self.kwargs[patient_id]=', self.kwargs['patient_id'])
        kwargs = super(PatientUpdateProfile, self).get_context_data(**kwargs)
        # get patient using patient_id
        access_token = utility.get_token()
        patient_api = PatientEndpoint(access_token)
        patient = patient_api.fetch(id=str(self.kwargs['patient_id']))
        patient = utility.convert_unicode_to_string(patient)
        print('cellphone = ', patient['cell_phone'])
        kwargs['patient'] = patient
        return kwargs

    def form_valid(self, form):
        """
            update patient info.
            if patient already has an appointment, mark status as arrived
            else create an appointment and mark status as arrived
         """
        print('\n \n form VALID !!')
        todays_date = date.today()
        access_token = utility.get_token()
        patient_api = PatientEndpoint(access_token)

        # update patient demographics
        update_resp = patient_api.update(
            id=str(self.kwargs['patient_id']),
            data=form.cleaned_data
        )

        # check if this patient has an appointment
        appnt_api = AppointmentEndpoint(access_token)
        appnt_list = list(appnt_api.list(
            date=todays_date,
            params={
                'patient': self.kwargs['patient_id']
            },
        ))
        print()
        print('appnt_list={}'.format(appnt_list))

        # if appnt doesnt exist create one
        if appnt_list == []:
            new_appt = appnt_api.create(
                data={
                    'date': todays_date,
                    'patient': self.kwargs['patient_id']
                }

            )

            print()
            print('new_appt={}'.format(new_appt))

        return super(PatientUpdateProfile, self).form_valid(form)

    def form_invalid(self, form):
        # Add action to invalid form phase
        print('Form INVALID \nself.request.POST = {}'.format(self.request.POST))
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('patient_update_profile', kwargs={'patient_id': self.kwargs['patient_id']})
