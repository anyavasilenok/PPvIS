from model import*
from view import*
from controller import*

if __name__ == "__main__":
    model = Model()
    controller = Controller(model);
    Clinic(model, controller).run()
