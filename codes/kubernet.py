class EC2Instance:
    def __init__(self, instance_id):
        self.instance_id = instance_id
        self.state = "running"

    def terminate(self):
        self.state = "terminated"
        print(f"Instance {self.instance_id} terminated.")

    def __str__(self):
        return f"Instance ID: {self.instance_id}, State: {self.state}"

class ECSCluster:
    def __init__(self, cluster_name):
        self.cluster_name = cluster_name
        self.tasks = []
        self.services = []

    def deploy_task(self, task_definition):
        self.tasks.append(task_definition)
        print(f"Task {task_definition} deployed in ECS Cluster {self.cluster_name}.")

    def scale_service(self, service_name, desired_count):
        for service in self.services:
            if service['name'] == service_name:
                service['desired_count'] = desired_count
                print(f"Service {service_name} scaled to {desired_count} in ECS Cluster {self.cluster_name}.")
                return
        print(f"Service {service_name} not found in ECS Cluster {self.cluster_name}.")

    def delete_task(self, task_definition):
        if task_definition in self.tasks:
            self.tasks.remove(task_definition)
            print(f"Task {task_definition} removed from ECS Cluster {self.cluster_name}.")
        else:
            print(f"Task {task_definition} not found in ECS Cluster {self.cluster_name}.")

    def __str__(self):
        return f"ECS Cluster {self.cluster_name}, Tasks: {self.tasks}, Services: {self.services}"

class KubernetesCluster:
    def __init__(self, cluster_name):
        self.cluster_name = cluster_name
        self.deployments = []
        self.services = []

    def deploy_pod(self, pod_definition):
        self.deployments.append(pod_definition)
        print(f"Pod {pod_definition} deployed in Kubernetes Cluster {self.cluster_name}.")

    def scale_deployment(self, deployment_name, replicas):
        for deployment in self.deployments:
            if deployment['name'] == deployment_name:
                deployment['replicas'] = replicas
                print(f"Deployment {deployment_name} scaled to {replicas} in Kubernetes Cluster {self.cluster_name}.")
                return
        print(f"Deployment {deployment_name} not found in Kubernetes Cluster {self.cluster_name}.")

    def delete_pod(self, pod_definition):
        if pod_definition in self.deployments:
            self.deployments.remove(pod_definition)
            print(f"Pod {pod_definition} removed from Kubernetes Cluster {self.cluster_name}.")
        else:
            print(f"Pod {pod_definition} not found in Kubernetes Cluster {self.cluster_name}.")

    def __str__(self):
        return f"Kubernetes Cluster {self.cluster_name}, Deployments: {self.deployments}, Services: {self.services}"

class EC2Manager:
    def __init__(self):
        self.instances = []
        self.instance_counter = 0

    def create_instance(self):
        self.instance_counter += 1
        instance_id = f"i-{self.instance_counter:04d}"
        instance = EC2Instance(instance_id)
        self.instances.append(instance)
        print(f"EC2 Instance {instance_id} created.")
        return instance_id

    def terminate_instance(self, instance_id):
        for instance in self.instances:
            if instance.instance_id == instance_id:
                instance.terminate()
                self.instances.remove(instance)
                return
        print(f"Instance {instance_id} not found.")

    def list_instances(self):
        print("EC2 Instances:")
        for instance in self.instances:
            print(instance)

def main():
    ec2_manager = EC2Manager()
    ecs_cluster = ECSCluster("ECS_Cluster_1")
    k8s_cluster = KubernetesCluster("K8S_Cluster_1")

    while True:
        print("\nCommands: create_instance, terminate_instance, deploy_task, scale_service, delete_task, deploy_pod, scale_deployment, delete_pod, list_instances, list_clusters, exit")
        command = input("Enter command: ").strip()

        if command == "create_instance":
            ec2_manager.create_instance()
        elif command == "terminate_instance":
            instance_id = input("Enter instance ID to terminate: ").strip()
            ec2_manager.terminate_instance(instance_id)
        elif command == "deploy_task":
            task_definition = input("Enter task definition: ").strip()
            ecs_cluster.deploy_task(task_definition)
        elif command == "scale_service":
            service_name = input("Enter service name: ").strip()
            desired_count = int(input("Enter desired count: ").strip())
            ecs_cluster.scale_service(service_name, desired_count)
        elif command == "delete_task":
            task_definition = input("Enter task definition to delete: ").strip()
            ecs_cluster.delete_task(task_definition)
        elif command == "deploy_pod":
            pod_definition = input("Enter pod definition: ").strip()
            k8s_cluster.deploy_pod(pod_definition)
        elif command == "scale_deployment":
            deployment_name = input("Enter deployment name: ").strip()
            replicas = int(input("Enter number of replicas: ").strip())
            k8s_cluster.scale_deployment(deployment_name, replicas)
        elif command == "delete_pod":
            pod_definition = input("Enter pod definition to delete: ").strip()
            k8s_cluster.delete_pod(pod_definition)
        elif command == "list_instances":
            ec2_manager.list_instances()
        elif command == "list_clusters":
            print(ecs_cluster)
            print(k8s_cluster)
        elif command == "exit":
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
