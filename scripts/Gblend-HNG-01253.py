hng_id = 'HNG-01253'
fullName = 'Ilochi Gabriel'
language = 'Python'
email = 'gabrielilo190@gmail.com'

def task_output(name, hngID, email, language):
    return  print('Hello World, this is {name} with HNGi7 ID {hngID} and email {email} using {language} for stage 2 task'.format(name=name, hngID=hngID, email=email, language=language))


task_output(fullName, hng_id, email, language)