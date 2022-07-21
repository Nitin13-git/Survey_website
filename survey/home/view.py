from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from home.models import SurveyTable
from django.contrib import messages


#create your view here
def index(request):
    context={}
    if request.method == "POST":
        try:
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            gender = request.POST["Gender"]
            city =  request.POST["City"]
            from_date = request.POST["from_date"]
            to_date = request.POST["to_date"]
            survey_data = SurveyTable(first_name=first_name, last_name=last_name, gender=gender, city=city, from_date=from_date, to_date=to_date)
            survey_data.save()
            messages.success(request, "Survey has been saved successfully!")
        except: "Enter the value again"
        context = {}
    return render(request,'index.html',context)


def dashboard(request):
    survey_content = {}
    if request.method == "POST":
        try:
            gender = request.POST["Gender"]
        except: gender = None
        try: 
            city =  request.POST["City"]
        except: city = None 
        try:
            from_date = request.POST["from_date"]
        except: from_date = None
        try:
            to_date = request.POST["to_date"]
        except: to_date = None

        if (gender != "" and gender != None) and (city != "" and city != None) and (from_date != "" and from_date != None) and (to_date != "" and to_date != None):
            survey_data = SurveyTable.objects.filter(gender=gender, city=city, from_date=from_date, to_date=to_date)

        elif (gender != "" and gender != None) and (city != "" and city != None):
            survey_data = SurveyTable.objects.filter(gender=gender, city=city)

        elif gender != "" and gender != None:
            survey_data = SurveyTable.objects.filter(gender=gender)

        elif city != "" and city != None:
            survey_data = SurveyTable.objects.filter(city=city)

        elif (from_date != "" and from_date != None) and (to_date != "" and to_date != None):
            survey_data = SurveyTable.objects.filter(from_date=from_date, to_date=to_date)

        elif from_date != "" and from_date != None:
            survey_data = SurveyTable.objects.filter(from_date=from_date) 

        else:
            messages.success(request, "You have to fill atleast any one of these form value!")
        messages.success(request, f"Total Rows Found: {len(survey_data)}!")
        survey_content = {
            "list_of_rows": survey_data
        }
    
    return render(request, "dashboard.html", survey_content)



