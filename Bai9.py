#bai9
def number_to_words(number):
    #dinh nghia cac so tu 1 den 19
    ones = ["", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin", "muoi", "muoi mot", "muoi hai", "muoi ba", "muoi bon", "muoi lam", "muoi sau", "muoi bay","muoi tam", "muoi chin"]
    #dinh nghia cac tu hang tram
    hundreds = ["", "mot tram", "hai tram", "ba tram", "bon tram", "namw tram", "sau tram", "bay tram", "tam tram", "chin tram"]
    if number == 0:
        return "khong"
    elif number < 20:
        return ones[number]
    elif number < 100:
        tens_digit = number // 10
        ones_digit = number % 10
        return ones[tens_digit] + " muoi " + ones[ones_digit]
    else:
        hundreds_digit = number // 100
        remainder = number % 100
        return hundreds[hundreds_digit] + " " + number_to_words(remainder)
    
def main():
    number = int(input("nhap 1 so tu 1 den 999: "))
    if 1 <= number <= 999:
        words = number_to_words(number)
        print(f"{number} duoc viet thanh chu la: {words}")
    else:
        print("so ban nhap khong hop le!")

if __name__ == "__main__":
    main()