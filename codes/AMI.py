class AMI:
    def __init__(self, ami_id, source_instance_id):
        self.ami_id = ami_id
        self.source_instance_id = source_instance_id

    def __str__(self):
        return f"AMI ID: {self.ami_id}, Source Instance ID: {self.source_instance_id}"

class EC2Instance:
    def __init__(self, instance_id, ami_id):
        self.instance_id = instance_id
        self.ami_id = ami_id
        self.state = "stopped"

    def start(self):
        if self.state == "stopped":
            self.state = "running"
            print(f"Instance {self.instance_id} started.")
        else:
            print(f"Instance {self.instance_id} is already running.")

    def stop(self):
        if self.state == "running":
            self.state = "stopped"
            print(f"Instance {self.instance_id} stopped.")
        else:
            print(f"Instance {self.instance_id} is not running.")

    def terminate(self):
        self.state = "terminated"
        print(f"Instance {self.instance_id} terminated.")

    def __str__(self):
        return f"Instance ID: {self.instance_id}, AMI ID: {self.ami_id}, State: {self.state}"

class EC2Simulator:
    def __init__(self):
        self.instances = {}
        self.amis = {}
        self.instance_counter = 0
        self.ami_counter = 0

    def create_instance(self, ami_id):
        self.instance_counter += 1
        instance_id = f"i-{self.instance_counter:04d}"
        instance = EC2Instance(instance_id, ami_id)
        self.instances[instance_id] = instance
        print(f"Instance {instance_id} created from AMI {ami_id}.")
        return instance_id

    def create_ami(self, source_instance_id):
        if source_instance_id in self.instances:
            self.ami_counter += 1
            ami_id = f"ami-{self.ami_counter:04d}"
            ami = AMI(ami_id, source_instance_id)
            self.amis[ami_id] = ami
            print(f"AMI {ami_id} created from Instance {source_instance_id}.")
            return ami_id
        else:
            print(f"Source instance {source_instance_id} not found.")
            return None

    def list_amis(self):
        print("Available AMIs:")
        for ami_id, ami in self.amis.items():
            print(ami)

    def list_instances(self):
        print("Instances:")
        for instance_id, instance in self.instances.items():
            print(instance)

    def start_instance(self, instance_id):
        if instance_id in self.instances:
            self.instances[instance_id].start()
        else:
            print(f"Instance {instance_id} not found.")

    def stop_instance(self, instance_id):
        if instance_id in self.instances:
            self.instances[instance_id].stop()
        else:
            print(f"Instance {instance_id} not found.")

    def terminate_instance(self, instance_id):
        if instance_id in self.instances:
            self.instances[instance_id].terminate()
        else:
            print(f"Instance {instance_id} not found.")

def main():
    simulator = EC2Simulator()

    while True:
        print("\nCommands: create_ami, create_instance, list_amis, list_instances, start, stop, terminate, exit")
        command = input("Enter command: ").strip()

        if command == "create_ami":
            instance_id = input("Enter source instance ID: ").strip()
            simulator.create_ami(instance_id)
        elif command == "create_instance":
            ami_id = input("Enter AMI ID: ").strip()
            simulator.create_instance(ami_id)
        elif command == "list_amis":
            simulator.list_amis()
        elif command == "list_instances":
            simulator.list_instances()
        elif command == "start":
            instance_id = input("Enter instance ID: ").strip()
            simulator.start_instance(instance_id)
        elif command == "stop":
            instance_id = input("Enter instance ID: ").strip()
            simulator.stop_instance(instance_id)
        elif command == "terminate":
            instance_id = input("Enter instance ID: ").strip()
            simulator.terminate_instance(instance_id)
        elif command == "exit":
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
