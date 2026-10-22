# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18

def main():
    calendar_years = input("Enter an age in calendar years: ")
    calendar_years = float(calendar_years)
    dog_years = calendar_years * DOG_YRS_MULTIPLIER
    dog_years = round(dog_years, 2)
    print("that's " +str(dog_years) +" in dog years!")

if __name__ == '__main__':
    main()
