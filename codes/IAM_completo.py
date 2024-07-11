import random
import uuid
import json

# Clases y definiciones
class IAMService:
    def __init__(self):
        self.users = {}
        self.groups = {}
        self.policies = {}
        self.roles = {}

class Policy:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

class IAMConsole:
    def create_user(self, iam_service, user_name):
        iam_service.users[user_name] = {'policies': [], 'mfa_enabled': False}
        print(f"User '{user_name}' created.")

    def create_group(self, iam_service, group_name):
        iam_service.groups[group_name] = {'policies': [], 'users': []}
        print(f"Group '{group_name}' created.")

# Inicialización del servicio y la consola
iam_service = IAMService()
iam_console = IAMConsole()

# Creación de usuarios y grupos
iam_console.create_user(iam_service, "alice")
iam_console.create_group(iam_service, "admin-group")

# Listar usuarios y grupos
def list_users(iam_service):
    return list(iam_service.users.keys())

def list_groups(iam_service):
    return list(iam_service.groups.keys())

print("Users:", list_users(iam_service))
print("Groups:", list_groups(iam_service))

# Gestión de usuarios y grupos
def add_user_to_group(iam_service, user_name, group_name):
    if user_name in iam_service.users and group_name in iam_service.groups:
        iam_service.groups[group_name]['users'].append(user_name)
        print(f"User '{user_name}' added to group '{group_name}'.")

def assign_policy_to_user(iam_service, user_name, policy):
    if user_name in iam_service.users:
        iam_service.users[user_name]['policies'].append(policy)
        print(f"Policy assigned to user '{user_name}'.")

def assign_policy_to_group(iam_service, group_name, policy):
    if group_name in iam_service.groups:
        iam_service.groups[group_name]['policies'].append(policy)
        print(f"Policy assigned to group '{group_name}'.")

add_user_to_group(iam_service, "alice", "admin-group")

# Definición de políticas
admin_policy = Policy("AdminPolicy", ["s3:ListBucket", "ec2:StartInstances"])
group_admin_policy = Policy("GroupAdminPolicy", ["s3:*", "ec2:*"])

iam_service.policies["AdminPolicy"] = admin_policy
iam_service.policies["GroupAdminPolicy"] = group_admin_policy

assign_policy_to_user(iam_service, "alice", admin_policy)
assign_policy_to_group(iam_service, "admin-group", group_admin_policy)

# Habilitación de MFA
def enable_mfa_for_user(iam_service, user_name):
    if user_name in iam_service.users:
        iam_service.users[user_name]['mfa_enabled'] = True
        print(f"MFA enabled for user '{user_name}'.")

enable_mfa_for_user(iam_service, "alice")

# Configuración de MFA
def setup_mfa(user_name):
    code = random.randint(100000, 999999)
    print(f"MFA setup for user '{user_name}'. Verification code: {code}")
    return code

correct_code = setup_mfa("alice")

# Políticas de contraseña
def set_password_policy(min_length, require_symbols, require_numbers):
    policy = {
        "min_length": min_length,
        "require_symbols": require_symbols,
        "require_numbers": require_numbers
    }
    print("Password policy set:", policy)

set_password_policy(8, True, True)

# Asignación de políticas adicionales
read_only_policy = Policy("ReadOnlyPolicy", ["s3:GetObject"])
write_policy = Policy("WritePolicy", ["s3:PutObject"])

iam_service.policies["ReadOnlyPolicy"] = read_only_policy
iam_service.policies["WritePolicy"] = write_policy

assign_policy_to_user(iam_service, "alice", read_only_policy)
assign_policy_to_group(iam_service, "admin-group", write_policy)

# Ejemplo de política IAM
example_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::example_bucket"
        }
    ]
}

def assign_json_policy_to_user(iam_service, user_name, policy_json):
    if user_name in iam_service.users:
        iam_service.users[user_name]['policies'].append(policy_json)
        print(f"JSON policy assigned to user '{user_name}'.")

assign_json_policy_to_user(iam_service, "alice", example_policy)

# Credenciales temporales
def generate_temporary_credentials():
    access_key = str(uuid.uuid4())
    secret_key = str(uuid.uuid4())
    session_token = str(uuid.uuid4())
    print(f"Temporary credentials generated:\nAccess Key: {access_key}\nSecret Key: {secret_key}\nSession Token: {session_token}")

generate_temporary_credentials()

# Informe de credenciales
def generate_credential_report(iam_service):
    report = {}
    for user in iam_service.users:
        report[user] = {
            "policies": iam_service.users[user]['policies'],
            "mfa_enabled": iam_service.users[user]['mfa_enabled']
        }
    print("Credential Report:", report)

generate_credential_report(iam_service)

# Ejercicios adicionales

# Gestión avanzada de políticas y permisos
def has_permission(iam_service, user_name, action, resource):
    if user_name in iam_service.users:
        user_policies = iam_service.users[user_name]['policies']
        for policy in user_policies:
            if isinstance(policy, Policy):
                if action in policy.permissions:
                    return True
            elif isinstance(policy, dict):
                for statement in policy['Statement']:
                    if action == statement['Action'] and resource == statement['Resource']:
                        return True
        for group_name in iam_service.groups:
            if user_name in iam_service.groups[group_name]['users']:
                group_policies = iam_service.groups[group_name]['policies']
                for policy in group_policies:
                    if isinstance(policy, Policy):
                        if action in policy.permissions:
                            return True
                    elif isinstance(policy, dict):
                        for statement in policy['Statement']:
                            if action == statement['Action'] and resource == statement['Resource']:
                                return True
    return False

print("Has permission:", has_permission(iam_service, "alice", "s3:ListBucket", "arn:aws:s3:::example_bucket"))

# Simulación completa de MFA
def verify_mfa(user_name, input_code, correct_code):
    if input_code == correct_code:
        print(f"MFA verified for user '{user_name}'.")
        return True
    else:
        print(f"MFA verification failed for user '{user_name}'.")
        return False

input_code = int(input("Enter the MFA code: "))
verify_mfa("alice", input_code, correct_code)

# Políticas basadas en condiciones
def assign_time_based_policy(iam_service, user_name, policy, start_hour, end_hour):
    current_hour = 12  # Simulación de la hora actual
    if start_hour <= current_hour < end_hour:
        assign_policy_to_user(iam_service, user_name, policy)
        print(f"Policy '{policy.name}' assigned to user '{user_name}' based on time condition.")

assign_time_based_policy(iam_service, "alice", admin_policy, 9, 17)

# Roles y credenciales temporales
def assume_role(iam_service, user_name, role_name):
    if role_name in iam_service.roles:
        role = iam_service.roles[role_name]
        generate_temporary_credentials()
        print(f"User '{user_name}' assumed role '{role_name}' with permissions: {role.permissions}")

iam_service.roles["admin-role"] = Policy("AdminRole", ["s3:*", "ec2:*"])
assume_role(iam_service, "alice", "admin-role")

# Informe detallado de credenciales y seguridad
def generate_detailed_credential_report(iam_service):
    report = {}
    for user in iam_service.users:
        user_policies = []
        for policy in iam_service.users[user]['policies']:
            if isinstance(policy, Policy):
                user_policies.append(policy.name)
            elif isinstance(policy, dict):
                user_policies.append(policy['Version'])
        report[user] = {
            "policies": user_policies,
            "mfa_enabled": iam_service.users[user]['mfa_enabled'],
            "roles": []
        }
        for role_name in iam_service.roles:
            if user in iam_service.roles[role_name].permissions:
                report[user]['roles'].append(role_name)
    print("Detailed Credential Report:", json.dumps(report, indent=2))

generate_detailed_credential_report(iam_service)
