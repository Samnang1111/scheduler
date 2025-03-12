# Task 2
import heapq

class JobScheduler:
    def __init__(self):
        self.jobs = []  # Min-heap to store jobs as (priority, job_name)
        
    def add_job(self, priority, job_name):
        """Adds a job to the job queue with the given priority."""
        heapq.heappush(self.jobs, (priority, job_name))  # Add a set of (priority, job_name) to the empty job list
        print(f"Job '{job_name}' with priority {priority} added.")
        
    def execute_job(self):
        """Removes and executes the job with the highest priority (lowest number)."""
        if self.jobs:
            priority, job_name = heapq.heappop(self.jobs)
            print(f"Executing job: {job_name} (Priority: {priority})")
        else:
            print("No jobs to execute!")
            
    def show_jobs(self):
        """Displays all jobs sorted by priority."""
        if self.jobs:
            print("Current job queue (sorted by priority):")
            for priority, job_name in sorted(self.jobs):
                print(f"- {job_name} (Priority: {priority})") 
        else:
            print("No jobs in the queue!")
     
# Example Usage
# scheduler = JobScheduler()

# scheduler.add_job(1, "Brush Teeth")
# scheduler.add_job(2, "Take a Shower")
# scheduler.add_job(3, "Go to School")

# scheduler.execute_job()

# scheduler.show_jobs()

def main():
    """Runs an interactive job scheduling system."""
    # Create the scheduler
    scheduler = JobScheduler()
    
    while True:
        print("\n--- Job Scheduling System Management ---")
        print("1. Add Job")
        print("2. Execute Job")
        print("3. Show Jobs")
        print("4. Exit")
        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                job_input = input("Enter job name: ")
                priority_input = int(input("Enter job priority (lower number = higher priority): "))
                scheduler.add_job(priority_input, job_input)  # Fixed argument order
            elif choice == 2:
                scheduler.execute_job()
            elif choice == 3:
                scheduler.show_jobs()
            elif choice == 4:
                print("Exiting Job Scheduler. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()