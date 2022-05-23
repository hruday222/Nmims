def interview(stu_list, total_time):
    time_list = [5,5,10,10,15,15,20,20]
    count = 0
    max_time = 120

    if len(stu_list) != len(time_list):
        return "Disqualified"
    elif total_time > max_time:
        return "Disqualified"
    else:
        for i in range(0, len(stu_list)):
            if stu_list[i] <= time_list[i]:
                count += 1 
            
        if count == len(stu_list):
            return "Qualified"
        else:
            return "Disqualified"

print(interview([5,5,10,10,15,15,20,20], 120))



    

