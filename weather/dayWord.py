#модуль возвращает текстовое обозначение 
# дня недели по его номеру

def DayA(NumDay):
    dicWeekday={0:'Пн',1:'Вт',2:'Ср',3:'Чт',4:'Пт',5:'Сб',6:'Вс'}
    DayWord=dicWeekday.get(NumDay)
    return DayWord