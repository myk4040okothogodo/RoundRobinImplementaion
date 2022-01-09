#python3 program from implementation of RR scheduliing

#function to find the waiting time for all processes
class RoundRobin:
    # calculate waiting time of given process by using quantum time
    def find_waiting_time(slf, processes, bt, wt, quantum,n):
        #Auxiliary space which is used to find waiting time
        pending_bt = [0]*n
        #Loop controlling variable
        i = 0
        #Get burst time
        while(i< n):
            pending_bt[i] = bt[i]
            i += 1

        # current time
        process_time = 0
        # work process indicator
        work = True
        #Execute round robin process
        # untill work are not complete
        while (work == True):
            #set that initial no work at this time
            work = False
            # Execute process one by one repeatedly
            i = 0
            while (i < n):
                if (pending_bt[i] > 0):
                    #when pending process exists
                    #activate work
                    work = True
                    if (pending_bt[i] > quantum):
                        #update the process_time
                        process_time += quantum
                        #Reduce padding burst time of current process
                        pending_bt[i] -= quantum
                    else:
                        #and the remains padding BT (burst time)
                        process_time = process_time + pending_bt[i]
                        #Get waiting time of i process
                        wt[i] = process_time - bt[i]
                        # set that no remaining pending time
                        pending_bt[i] = 0

            i += 1

            #This is calculating the average time by using given processes id, burst time and quantum
    def find_avg_time(self, processes, burst_time, quantum, n):
        #Auxiliary space to store waaiting time and turnaround time
        turnaround_time = [0]* n
        waiting_time = [0]* n
        # Resultant variable
        total_waiting_time = 0
        total_turnaround_time = 0
        # Loop control varibale
        i = 0
        self.find_waiting_time(processes, burst_time, waiting_time, quantum, n)
        # calculate turnaround time
        while (i < n):
            # Get turn around time for ith processes
            turnaround_time [i] = burst_time[i] + waiting_time[i]
            i += 1
        print ("(Process)( Burst Time)( Turn Around Time)", end="")
        #Display process, burst time, waiting time, turn around time
        #And calculate the average waiting time and average turn around time
        i = 0
        while (i < n):
            #calculate waiting time
            total_waiting_time += waiting_time[i]
            #calculate turnaround time
            total_turnaround_time += turnaround_time[i]
            print("\n p", process[i], "\t\t", burst_time[i], "\t\t", waiting_time[i],"\t\t", turnaround_time[i], end="")
            i += 1
        print ("\n Avearage Waiting Time : ", (total_waiting_time / n))
        print (" Average Turn Around Time : ", (total_turnaround_time /n))


def main():
    obj = RoundRobin()
    #Process set
    processes = [1, 2, 3, 4]
    #Burst time of process set
    burst_time = [4, 3, 5, 9]
    # Assume that size  of process and burst time is equal
    # Get size
    n = len(processes)
    quantum = 2
    obj.find_avg_time(processes, burst_time, quantum, n)


if __name__ == "__main__": main()    
        
