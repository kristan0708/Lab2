print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

"""
def funcName(parameter1, parameter2):
    print("this is a dummy function")
    return 10

"""

def main():
    display_main_menu()
    float_list = get_user_input()
    sort_temp = sort_temperature(float_list)
    median = float(calc_median_temperature(sort_temp))
    print(median)


def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input(":")
    string_list = user_input.split(",")
    float_list = []

    for num_str in string_list:
        float_list.append(float(num_str))
    return float_list

def calc_average(list_float_num):
    avg = float(sum(list_float_num) / len(list_float_num))
    return avg

def sort_temperature(temp_list):
    sorted_temp = sorted(temp_list)
    return sorted_temp

def find_min_max(list_float_num):
    min_max = [int(min(list_float_num)),int(max(list_float_num))]
    return min_max

def calc_median_temperature(median_temp):
    if len(median_temp)%2 == 0:
        sum_median = float(median_temp[(len(median_temp)//2)] + median_temp[(len(median_temp)//2 - 1)])
        median = sum_median/2
    else:
        index = round(len(median_temp)//2)
        median = float(median_temp[index])

    return median

if __name__ == '__main__':
    main()