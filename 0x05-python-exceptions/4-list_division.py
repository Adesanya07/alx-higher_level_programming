#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    switch = 0
    for i in range(list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            switch = 1
        except TypeError:
            print("wrong type")
            switch = 1
        except IndexError:
            print("out of range")
            switch = 1
        finally:
            if switch:
                switch = 0
                result_list.append(0)
            else:
                result_list.append(x)
    return result_list
            
                            

                     
