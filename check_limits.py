import sys  

no_para = 3

Battery_range= [[0,45], [20,80], [-sys.maxsize,0.8]]
Battery_parameters =['temperature', 'soc', 'charge_rate'] 

def breach_L_H(Battery_readings):
  Reading_status=['n','n','n']
  for i in range(0, no_para):
    print(Battery_range[i], Battery_readings[i])
    if (Battery_readings[i])<(Battery_range[i][0]):
      Reading_status[i]='L'
      
    elif (Battery_readings[i])>(Battery_range[i][1]):
      Reading_status[i]='H'
      
  print(Reading_status)
  return Reading_status
    

def battery_is_ok(Battery_readings):
  Reading_status=breach_L_H(Battery_readings)
  print(Reading_status)
  if 'L' in Reading_status or 'H' in Reading_status:
    return False
  else:
    return True


if __name__ == '__main__':
  assert(battery_is_ok([25, 70, 0.7]) is True)
  assert(battery_is_ok([50, 85, 0]) is False)
