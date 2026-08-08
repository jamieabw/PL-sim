from pl_predictor.gui.app import App


def main():
    gui = App()

#TODO: make threads work so the UI doesnt freeze during simulations, with some form of callback to the main thread so it updates to say what sim currently on etc

if __name__ == "__main__":
    main()