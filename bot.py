from math import gcd
from time import sleep
def findHCF(list: list):
    HCF = gcd(list[0], list[1])
    for i in list[2:]:
        HCF = gcd(HCF, i)
    return HCF


def findLCM(list: list):
    LcmTwoArgs = lambda x, y: int((x * y)/gcd(x, y))
    LCM = LcmTwoArgs(list[0], list[1])
    for i in list[2:]:
        LCM = LcmTwoArgs(LCM, i)
    return LCM


class bot():
    def __init__(self, options: list, controller_obj):
        self.keyboard = controller_obj
        self.proceed = True

        self.options = options
        self.reset_times = [i["reset_time"] for i in options] # List of reset times
        LCM_time = findLCM(self.reset_times) # Length of one loop (in seconds)
        self.pulse_time = findHCF(self.reset_times) # Length of each pulse
        self.total_pulses = int(LCM_time / self.pulse_time) # Total no. of pulses in one loop

        self.pulse_count = 0 # Total no. of pulses ran
    
    @property
    def order(self):
        intervals = [int(i / self.pulse_time) for i in self.reset_times] # Pulse intervals necessary 
        order_list = []
        # for each pulse
        for i in range(1, self.total_pulses + 1):
            pulse_index = [x for x in range(len(intervals)) if int(i % intervals[x]) == 0]
            order_list.append(pulse_index)
        return order_list

    @property
    def runtime(self):
        return self.pulse_count * (15 + 4*0.5)

    def run_cycle(self):
        if self.pulse_count == 0:
            for i in range(len(self.options)):
                self.keyboard.type(self.options[i]["command"]())
                sleep(0.5)

        for i in range(self.total_pulses):
            if self.proceed:
                self.pulse_count += 1 # Increments the count of total pulses ran
                sleep(self.pulse_time)
                for x in self.order[i]:
                    self.keyboard.type(self.options[x]["command"]())
                    sleep(0.5)
