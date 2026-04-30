def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / height**2

    print(f"Your bmi is {bmi:.2f}")

    if bmi<18.5:
        print("Your Underweight!")
    elif bmi>25:
        print("Your Over Weight!")
    else:
        print("Your Normal Weight :)")


calculate_bmi(weight = float(input("What is your weight in kg: ")),height = float(input("What is your height (in meters): ")))