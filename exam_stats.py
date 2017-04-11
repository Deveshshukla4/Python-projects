def main():
    grades = [60, 80, 90, 90, 90, 80] #list of grades

    def print_grades(grades): #print list of grades
        for grade in grades:
            print " " + str(grades)


    def grades_sum(grades): #Total of grades
        total = 0
        for grade in grades:
            total += grade
        return total

    def grades_average(grades): #Average of grades
        sum_of_grades = grades_sum(grades)
        average = sum_of_grades / float(len(grades))
        return average

    def grades_variance(scores): # variance of grades
        average = grades_average(scores)
        variance = 0
        for score in scores:
            variance = variance + (average - score) **2
        variance = variance / len(scores)
        return variance


    def grades_std_deviation(variance): #deviation of grades
        return variance ** 0.5

    variance = grades_variance(grades)
    lists_of_grades = print_grades(grades)

    print "Grades " + str(lists_of_grades)
    print "Total " + str(grades_sum(grades))
    print "Average " + str(grades_average(grades))
    print "Variance " + str(variance)
    print "Standard Deviation " + str(grades_std_deviation(variance))
