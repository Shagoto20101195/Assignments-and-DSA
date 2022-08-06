#include <stdio.h>

int process[100][8];
int burst_copy[100];
int n;

int main()
{
    // process[row = number of processes][column = all times]
    // 0 = id
    // 1 = arrival
    // 2 = burst
    // 3 = start
    // 4 = end
    // 5 = waiting
    // 6 = turnaround
    // 7 = priority

    printf("Enter number of processes: ");
    scanf("%d", &n);

    int total_burst = 0;
    for(int i = 1; i<=n; i++)
    {
        process[i][0] = i;
        printf("Enter process %d arrival time,  burst time and priority: ", i);
        scanf("%d %d %d", &process[i][1], &process[i][2], &process[i][7]);

        process[i][3] = 0;
        process[i][4] = 0;
        process[i][5] = 0;
        process[i][6] = 0;
        burst_copy[i] = process[i][2];
        total_burst += process[i][2];
    }

    process[0][7] = 99999999;
    for(int i = 0; i<=total_burst; i++)
    {
        int max_priority_process = 0;

        // For finding the process with highest priority and also in the queue
        for(int j = 1; j<=n; j++)
        {
            if(process[j][2] > 0 && process[j][1] <= i && process[j][7] < process[max_priority_process][7])
            {
                max_priority_process = j;
            }
        }

        process[max_priority_process][2]--;

        // If burst changed, it means process started
        if(burst_copy[max_priority_process] - process[max_priority_process][2] == 1)
        {
            process[max_priority_process][3] = i + 1;
        }

        // Process finished, now to calculate end and turnaround time
        if(process[max_priority_process][2] == 0)
        {
            process[max_priority_process][4] = i + 1;
            process[max_priority_process][6] = process[max_priority_process][4] - process[max_priority_process][1];
        }

        // Waiting time calculation i.e. processes which are in queue and has remaining time that are
        // not being executed now
        for(int j = 1; j<=n; j++)
        {
            if(process[j][1] <= i && j != max_priority_process && process[j][2] > 0)
            {
                process[j][5]++;
            }
        }
    }



    for(int i = 1; i<=n; i++)
    {
        printf("Completion time for process %d: %d\n", process[i][0], process[i][4]);
        printf("Waiting time for process %d: %d\n", process[i][0], process[i][5]);
        printf("Turnaround time for process %d: %d\n\n", process[i][0], process[i][6]);
    }


    return 0;
}
