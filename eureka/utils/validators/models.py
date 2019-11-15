"""Validate fields CSV File."""

#Python
import string


#Django
from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect


def validate_fields(row,fila,new_values):
    """
    Valida cada campo de cada fila segun lo declarado en el modelo.
    Devuelve:
        - Un diccionario con los errores
        - #Fila analizada
        - Un diccionario key:value
        - Status de Error: True or False
    """
    # "Definiciones iniciales del diccionario de errores
    # y status de error.
    dict_error={}
    error_count = False

    """Validaciones de cada campo segun el modelo Job."""
    #Validate Job.id
    if row[0] == None:
        new_values['id'] =row[0]
        # dict_error['id'] = ''
    else:
        try:
            if isinstance(int(row[0]),int):
                new_values['id'] =row[0]
                # dict_error['id'] = ''
        except ValueError:
            error_count=True
            dict_error['id'] = ValueError('Error en id')

    #Validate Job.company_ruc
    if len(row[1])==11:
        new_values['company_ruc'] =row[1]
        # dict_error['company_ruc'] = ''
    else:
        error_count=True
        dict_error['company_ruc'] = ValidationError('Error en company_ruc')

    #Validate Job.company_name
    if len(row[2])<=100 and row[2] != None:
        new_values['company_name'] =row[2]
        # dict_error['company_name'] = ''
    else:
        error_count=True
        dict_error['company_name'] =  ValidationError('Error en company_name')

    #Validate Job.title
    if len(row[3])<=100 and row[3] != None:
        new_values['title'] =row[3]
        # dict_error['title'] = ''
    else:
        error_count=True
        dict_error['title'] = ValidationError('Error en title')

    #Validate Job.description
    if isinstance(row[4],str) and row[4] != None:
        new_values['description'] =row[4]
        # dict_error['description'] = ''
    else:
        error_count=True
        dict_error['description'] = ValidationError('Error en description')

    #Validate Job.requeriments
    if isinstance(row[5],str) and row[5] != None:
        new_values['requeriments'] =row[5]
        # dict_error['requeriments'] = ''
    else:
        error_count=True
        dict_error['requeriments'] =  ValidationError('Error en requeriments')

    #Validate Job.contact_email
    if row[6] != None:
        new_values['contact_email'] =row[6]
        # dict_error['contact_email'] = ''
    else:
        error_count=True
        dict_error['contact_email'] =  ValidationError('Error en contact email')

    #Validate Job.location
    if len(row[7])<=50 and row[7] != None:
        new_values['location'] =row[7]
        # dict_error['location'] = ''
    else:
        error_count=True
        dict_error['location'] =  ValidationError('Error en Location')

    #Validate Job.is_active
    if row[8] == None:
        new_values['is_active'] =row[8]
        # dict_error['is_active'] = ''
    else:
        try:
            if int(row[8])==1 or int(row[8])==0:
                new_values['is_active'] =row[8]
                # dict_error['is_active'] = ''
        except Exception as e:
            error_count=True
            dict_error['is_active'] =  ValidationError('Error en el is_active')

    #Validate Job.is_verified
    if row[9] == None:
        new_values['is_verified'] =row[9]
        # dict_error['is_verified'] = ''
    else:
        try:
            if int(row[9])==1 or int(row[9])==0:
                new_values['is_verified'] =row[9]
                # dict_error['is_verified'] = ''
        except Exception as e:
            error_count=True
            dict_error['is_verified'] =  ValidationError('Error en el is_verified')

    #Validate Job.is_public
    if row[10] == None:
        new_values['is_public'] =row[10]
        # dict_error['is_public'] = ''
    else:
        try:
            if int(row[10])==1 or int(row[10])==0:
                new_values['is_public'] =row[10]
                # dict_error['is_public'] = ''
        except Exception as e:
            error_count=True
            dict_error['is_public'] =  ValidationError('Error en el is_public')

    #Validate Job.show_recruiter
    if row[11] == None:
        new_values['show_recruiter'] =row[11]
        # dict_error['show_recruiter'] = ''
    else:
        try:
            if int(row[11])==1 or int(row[11])==0:
                new_values['show_recruiter'] =row[11]
                # dict_error['show_recruiter'] = ''
        except Exception as e:
            error_count=True
            dict_error['show_recruiter'] =  ValidationError('Error en el show_recruiter')

    #Validate Job.website_url
    if row[12] == None:
        new_values['website_url'] =row[12]
        # dict_error['website_url'] = ''
    else:
        if len(row[12])>4:
            new_values['website_url'] =row[12]
            # dict_error['website_url'] = ''
        else:
            error_count=True
            dict_error['website_url'] =  ValidationError('Error en website_url')

    #Validate Job.benefits
    if isinstance(row[13],str) or row[13] == None:
        new_values['benefits'] =row[13]
        # dict_error['benefits'] = ''
    else:
        error_count=True
        dict_error['benefits'] =  ValidationError('Error en benefits')

    #Validate Job.urgency
    if isinstance(row[14],str) or row[14] == None:
        new_values['urgency'] =row[14]
        # dict_error['urgency'] = ''
    else:
        error_count=True
        dict_error['urgency'] =  ValidationError('Error en urgency')

    #Validate Job.schedule
    if isinstance(row[15],str) or row[15] == None:
        new_values['schedule'] =row[15]
        # dict_error['schedule'] = ''
    else:
        error_count=True
        dict_error['schedule'] =  ValidationError('Error en schedule')

    #Validate Job.comment
    if isinstance(row[16],str) or row[16] == None:
        new_values['comment'] =row[16]
        # dict_error['comment'] = ''
    else:
        error_count=True
        dict_error['comment'] =  ValidationError('Error en comment')

    #Validate Job.min_salary
    if isinstance(row[17],int) or row[17] == None:
        new_values['min_salary'] =row[17]
        # dict_error['min_salary'] = ''
    else:
        error_count=True
        dict_error['min_salary'] =  ValidationError('Error en min_salary')

    #Validate Job.max_salary
    if isinstance(row[18],int) or row[18] == None:
        new_values['max_salary'] =row[18]
        # dict_error['max_salary'] = ''
    else:
        error_count=True
        dict_error['max_salary'] = ValidationError('Error en max_salary')

    #Validate Job.pay_range_period
    if row[19]=='al mes' or row[19]=='al año' or row[19] == None:
        new_values['pay_range_period'] =row[19]
        # dict_error['pay_range_period'] = ''
    else:
        error_count=True
        dict_error['pay_range_period'] =  ValidationError('Error en pay_range_period')

    return {"errors": dict_error,"fila":fila,"new_values":new_values,"error_status":error_count}
