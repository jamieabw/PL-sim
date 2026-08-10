from pl_predictor.gui.app import App
import sys

sys.setswitchinterval(0.001)

# TODO: change to multiprocessing rather than multithreading to solve issue with GIL

def main():
    gui = App()


if __name__ == "__main__":
    main()