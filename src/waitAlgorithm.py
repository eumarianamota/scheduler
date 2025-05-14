class WaitAlgorithm:
    def __init__(self, processes):
        self.processes = processes

    def SFJ(self):
        processes = sorted(self.processes, key=lambda x: x[1])

        waiting_time = 0
        for i in range(len(self.processes)):
            waiting_time += processes[i][1]
            processes[i].append(waiting_time)
        return processes

    def FIFO(self):
        processes = sorted(self.processes)

        waiting_time = 0
        for i in range(len(self.processes)):
            waiting_time += processes[i][1]
            processes[i].append(waiting_time)
        return processes

    def RR(self):
        return None
