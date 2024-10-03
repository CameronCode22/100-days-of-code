import datetime

def life_in_weeks(dob):
    #convert dob string to datetime object
    dob = datetime.datetime.strptime(dob, "%m/%d/%Y")

    #get today's date
    today_date = datetime.datetime.now()
    formatted_date = today_date.strftime("%m/%d/%Y") 
    print(formatted_date)

    # add 90 years to dob
    ninety_dob = dob.replace(year=dob.year +90)

    #format dob and 90-year date
    formated_ninety_dob = ninety_dob.strftime("%m/%d/%Y")


    print("Date when 90 years old:", formated_ninety_dob)

    weeks_left = abs((today_date - ninety_dob).days) // 7

    print(weeks_left)

life_in_weeks('10/22/1994')
