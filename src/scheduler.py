from waitAlgorithm import WaitAlgorithm


class Scheduler:
    def __init__(self):
        self.processes = []

    def receiveProcesses(self):
        for i in range(5):
            value = int(input("Qual a ordem do processo? "))
            size = int(input(f"Qual o  tamanho do processo {value}? "))
            self.processes.append([value, size])
        return self.processes

    def calculateWaitingTime(self):
        algorithm = int(input("Digite o número do escalonador de processo você quer utilizar: \n1- FIFO \n2- SFJ \n3- RR \n"))

        waitAlgorithm = WaitAlgorithm(self.processes)

        if algorithm == 1:
            waiting_time = waitAlgorithm.FIFO()
            return waiting_time
        elif algorithm == 2:
            waiting = waitAlgorithm.SFJ()
            return waiting
        elif algorithm == 3:
            waiting_time = waitAlgorithm.RR()
            return waiting_time

    def showWaitingTime(self):
        return None

    def calculateTurnAround(self):
        return None

    def showTurnAround(self):
        return None
