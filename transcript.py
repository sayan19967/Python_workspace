def transcript(coursedetails, studentdetails, grades):
    list = []
    studentdetails.sort()
    coursedetails.sort()
    grades.sort()
    for studentdet in studentdetails:
        tuple = studentdet
        inlist = []
        for grade in grades:
            if studentdet[0] == grade[0]:
                for cdetail in coursedetails:
                    if grade[1] == cdetail[0]:
                        intuple = cdetail
                        intuple = intuple + (grade[2],)
                        inlist.append(intuple)
        tuple = tuple + (inlist,)
        list.append(tuple)
    return list
