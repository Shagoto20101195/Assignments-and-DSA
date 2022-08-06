#include <stdio.h>

int process[100][6];
int burst_copy[100];
int n, q;

int main()
{
    // process[row = number of processes][column = all times]
    // 0 = id
    // 1 = burst
    // 2 = start
    // 3 = end
    // 4 = waiting
    // 5 = turnaround

    printf("Enter number of processes: ");
    scanf("%d", &n);

    printf("Enter time quantum: ");
    scanf("%d", &q);

    int total_burst = 0;
    for(int i = 1; i<=n; i++)
    {
        process[i][0] = i;
        printf("Enter process %d burst time: ", i);
        scanf("%d", &process[i][1]);

        process[i][2] = 0;
        process[i][3] = 0;
        process[i][4] = 0;
        process[i][5] = 0;
        burst_copy[i] = process[i][1];
        total_burst += process[i][1];
    }

    int current_process = 1;
    int count = 0;
    int finished = 0;
    for(int i = 0; i<=total_burst; i++)
    {
        // count is for keeping track of each round
        process[current_process][1]--;
        count++;

        // If burst changed, it means process started
        if(burst_copy[current_process] - process[current_process][1] == 1)
        {
            process[current_process][2] = i + 1;
        }

        // When a round is completed, need to change process
        if(count % q == 0)
        {
            // This is for when a round is completed and also a process is finished
            if(process[current_process][1] == 0)
            {
                goto label;
            }

            // Else find next process which has burst time remaining
            while(1)
            {
                current_process = (current_process + 1) % n;

                if(current_process == 0)
                {
                    current_process = n;
                }

                if(process[current_process][1] > 0)
                {
                    break;
                }
            }
            count = 0;
        }

        // Process finished, now to calculate end and turnaround time
        // This label is for when a process is finished and need to change process (if any available)
        label:
        if(process[current_process][1] == 0)
        {
            finished++;
            process[current_process][3] = i + 1;
            process[current_process][5] = process[current_process][3];

            while(process[current_process][1] == 0 && finished != n)
            {
                current_process = (current_process + 1) % n;

                if(current_process == 0)
                {
                    current_process = n;
                }
            }
            count = 0;
        }

        // Waiting time calculation i.e. processes which are in queue and has remaining time that are
        // not being executed now
        for(int j = 1; j<=n; j++)
        {
            if(j != current_process && process[j][1] > 0)
            {
                process[j][4]++;
            }
        }
    }



    for(int i = 1; i<=n; i++)
    {
        printf("Completion time for process %d: %d\n", process[i][0], process[i][3]);
        printf("Waiting time for process %d: %d\n", process[i][0], process[i][4]);
        printf("Turnaround time for process %d: %d\n\n", process[i][0], process[i][5]);
    }


    return 0;
}
