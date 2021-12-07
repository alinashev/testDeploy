from Action.Router import Router


def main():
    print("Hello jenkins!!!!")
    router = Router(1)
    router.generate_menu()
    router.selection_version()


if __name__ == '__main__':
    main()
