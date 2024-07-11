#4. Diferencias clave entre usuarios IAM y Grupos IAM
#Crear funciones para añadir usuarios a grupos y asignar políticas a usuarios y grupos.
class IAMService:
 def __init__(self):
  self.users = {"alice":[],"paco":[]}
  self.groups = {"admin-group":[],"otro_grupo":[]}
  self.policies = {"AdminPolicy":[]}
  self.roles = {"hola":[]}
iam_service = IAMService()

def add_user_to_group(iam_service, user_name, group_name):
  if user_name in iam_service.users and group_name in iam_service.groups:
    iam_service.groups[group_name].append(user_name)
    print(f"User '{user_name}' added to group '{group_name}'.")


def assign_policy_to_user(iam_service, user_name, policy):
  if user_name in iam_service.users:
    iam_service.users[user_name].append(policy)
    print(f"Policy assigned to user '{user_name}'.")


def assign_policy_to_group(iam_service, group_name, policy):
  if group_name in iam_service.groups:
    iam_service.groups[group_name].append(policy)
    print(f"Policy assigned to group '{group_name}'.")



add_user_to_group(iam_service, "alice", "admin-group")
add_user_to_group(iam_service, "paco", "otro_grupo")
assign_policy_to_user(iam_service, "alice", "AdminPolicy")
assign_policy_to_group(iam_service, "admin-group", "GroupAdminPolicy")

iam_service.users
iam_service.groups
iam_service.policies


print(iam_service.users)
print(iam_service.groups)
print(iam_service.policies)
print(iam_service.roles)
