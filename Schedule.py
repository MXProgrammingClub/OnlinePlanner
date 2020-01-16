# @author Lucas DeGreeff
class Day:
    """
    Defines a day within the schedule
    """
    day, blocks = 0, [] #day is 0-6, mon-sun
    def __init__(self, day, blocks):
        self.day = day
        self.blocks = blocks

    def sort_blocks(self):
        temp = []
        tempBlock = self.blocks[0]
        loop = len(self.blocks)
        for w in range(0, loop):
            for i in range(0, len(self.blocks)):
                if(self.blocks[i].get_start.compare(tempBlock.get_start) == False):
                    tempBlock = self.blocks[i]
            temp.append(tempBlock)
            self.blocks.remove(tempBlock)
            tempBlock = self.blocks[0]
        self.blocks = temp

    class Block:
        """
        Defines a block, such as Tuesday H or Friday F
        """
        class Time:
            """
            Defines a time, to be used for starts and ends of blocks
            """
            hour, minute, isPm = 12, 0, False
            #hour must be 0 < hour <= 12, minute must be 0 <= minute < 60, isPm must be a boolean
            def __init__(self, h, m, pm = False):
                self.hour = h
                self.minute = m
                self.isPm = pm
                if not (h > 0 and h <= 12):
                    self.hour = 12
                if not (m >= 0 and m < 60):
                    self.minute = 0

            #Assigns new value to minute variable
            def new_min(self, m):
                if m >= 0 and m < 60:
                    self.minute = m

            #Assigns new value to hour variable
            def new_hour(self, h):
                if h > 0 and h <= 12:
                    self.hour = h

            #Assigns new value to isPm attribute
            def change_pm(self, isPM):
                self.isPm = isPM

            #returns time min minutes later
            def mins_later(self, min):
                resMin = self.minute
                resHour = self.hour
                resMin += min
                resPM = self.isPm
                while resMin >= 60:
                    resMin -= 60
                    resHour += 1
                while resHour > 12:
                    resHour - 12
                    resPM = not resPM
                return Time(resHour, resMin, resPM)

            #Returns displayable string for the time, with or without the PM/AM
            def toString(self, include_PM = False):
                result = str(self.hour) + ':'
                if(self.minute < 10):
                    result += '0'
                result += str(self.minute)
                if(include_PM):
                    if(self.isPm):
                        result += ' ' + 'PM'
                    else:
                        result += ' ' + 'AM'
                return result
            #returns true if self is earlier than other
            #works only for times within the same day
            def compare(self, other):
                if(other.isPm() and not self.isPm()):
                    return self
                if(self.isPm() and not other.isPm()):
                    return other
                if(self.hour < other.hour):
                    return self
                if(self.hour > other.hour):
                    return other
                if(self.minute < other.minute):
                    return self
                else:
                    return other
        """
        time_start is the time that the block starts
        day is  a day stored as an int - 0 = mon ...  6 = sun
        time_end is the time of the end of the block, set to 40 min after start if no parameter
        is_test_day is a boolean for whether or not a block is a test day, and unless specified is false
        name is a string
        """
        name, day, time_start, time_end, is_test_day = "", 0, Time(0,0), Time(0,0), False

        def __init__(self, time_start, day, name, time_end = Time(0, 0), is_test_day = False):
            self.name = name
            self.day = day
            self.time_start = time_start
            if(time_end.equals(Time(0,0))):
                self.time_end = self.time_start.mins_later(40)
            else:
                self.time_end = time_end
            self.is_test_day = is_test_day

        def new_start(self, start):
            self.time_start = start

        def new_end(self, end):
            self.time_ends = end

        def new_day(self, new_day):
            self.days = new_day

        def new_name(self, name):
            self.name = name

        def get_start(self):
            return self.time_start

        def get_name(self):
            return self.name

        def get_day(self):
            return self.day

        def get_end(self):
            return self.time_end

        def is_test_day(self):
            return self.is_test_day
