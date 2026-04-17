from operation import Operation

operation = Operation()


while True:
    print('1. Dodaj książkę')
    print('2. Dodaj użytkownika')
    print('3. Wypożycz książkę')
    print('4. Oddaj książkę')
    print("5. Ureguluj opłatę")
    print("6. Stan konta")
    print('Q. Wyjdź')
    action: str = input('Podaj nr. akcji >')
    match action:
        case '1':

            operation.insert_book(input('Podaj tytuł książki >'),
                                  input('Podaj autora książki >'),
                                  input('Podaj rok wydania >'))

        case '2':
            operation.insert_user(input('Podaj imię użytkownika >'),
                                  input('Podaj nazwisko użytkownika >'),
                                  input("Podaj e-mail użytkownika >"))
        case '3':
            operation.rent_book(int(input('Podaj id użytkownika >')),
                                int(input('Podaj id książki >')))
        case '4':
            operation.return_book(int(input('Podaj id książki >')))
        case '5':
            pass
        case '6':
            pass
        case 'Q':
            break
        case "q":
            break

