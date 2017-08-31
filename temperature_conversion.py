def main():
    c= input("Do you want to continue?")
    loop(c)
def loop(c):
    if c == 'yes':
        print("Go ahead!")
        convert()
    else:
        print("Goodbye!")
def convert():
    temp = int(input("Please enter the temperature in Fahrenheit:"))
    v = (temp - 32) * 5 / 9     #converts the Fahrenheit into Celsius
    print("The temperature you entered in Fahrenheit is", temp)
    print("The temperature in Celsius is", "{0:.2f}".format(v))  #"{0:.2f}".format() sets the values in two decimal position
    main()
convert()