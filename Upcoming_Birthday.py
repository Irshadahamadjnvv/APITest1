import json 
import requests

base_url = "https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/"
remaining_url = "Prod/next-birthday?dateofbirth="
def upcoming_birthday(years_unit):
  '''
  Description: Used to find the amount of time left before user's next birthday.
  Params: years_unit: it is combination of years & unit
  Return: return amount of time remaining or raise error
  '''
  try:
    get_status=requests.get(base_url+remaining_url+years_unit)
    if get_status.status_code>201:
      try:
          error = get_status.json()
          print('API returned HTTP %s (%s)' % (get_status.status_code, error))
      except:
          print('API returned HTTP %s (%s)' % (get_status.status_code, get_status.content))
    else:
      try:
        return get_status.json()
      except: # Nothing to return
        return {}
  except Exception as e:
    print("Failed to parse URL or code due to : "+str(e))

testcases_input = ["1990-10-30&unit=hour","1990-10-30&unit=day","1990-10-30&unit=week","1990-10-30&unit=month"]
for yearsUnit in testcases_input:
  print("Just to check upcoming birthdays is after : "+str(upcoming_birthday(yearsUnit)))
print("Testcase verify with inputs provided below: ")

year_val = input("To get upcoming birthday please input years in format of 'YYYY-MM-DD'")
unit_val = input("To get upcoming birthday please unit values in format of 'hour','day','week','month'")
try:
  print("Upcoming birthdays is after : "+str(upcoming_birthday(str(year_val)+"&"+"unit="+unit_val)))
except Exception as e:
  print("Entered wrong format of years or unit values, please run again!")
