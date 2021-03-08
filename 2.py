time=int(input("Введите время, секунды"))
hours=time//3600
minutes=time//60-hours*60
sec=time-minutes*60-hours*3600
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {sec}")