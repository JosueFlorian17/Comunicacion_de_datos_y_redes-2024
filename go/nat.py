class SimpleNAT:
    def __init__(self, public_ip):
        self.public_ip = public_ip
        self.internal_to_external = {}
        self.external_to_internal = {}

    def assign_port(self, internal_ip):
        # Simple port assignment logic (could be improved)
        port = len(self.internal_to_external) + 1024  # Starting port range from 1024
        self.internal_to_external[(internal_ip, port)] = self.public_ip
        self.external_to_internal[(self.public_ip, port)] = internal_ip
        return port

    def translate_to_external(self, internal_ip, internal_port):
        if (internal_ip, internal_port) in self.internal_to_external:
            return self.public_ip, internal_port
        else:
            return None

    def translate_to_internal(self, external_ip, external_port):
        if (external_ip, external_port) in self.external_to_internal:
            return self.external_to_internal[(external_ip, external_port)]
        else:
            return None

    def simulate_traffic(self, internal_ip, internal_port, external_destination):
        external_ip, external_port = self.translate_to_external(internal_ip, internal_port)
        if external_ip:
            print(f"Internal {internal_ip}:{internal_port} -> {external_destination} via {external_ip}:{external_port}")
        else:
            print("Translation failed")

    def simulate_response(self, external_ip, external_port, response_source):
        internal_ip = self.translate_to_internal(external_ip, external_port)
        if internal_ip:
            print(f"Response from {response_source} to {external_ip}:{external_port} translated to {internal_ip}")
        else:
            print("Translation failed")

# Example usage
nat = SimpleNAT(public_ip="203.0.113.1")

# Assign ports to internal IPs
internal_ip1 = "192.168.0.2"
internal_port1 = nat.assign_port(internal_ip1)

internal_ip2 = "192.168.0.3"
internal_port2 = nat.assign_port(internal_ip2)

# Simulate traffic from internal to external
nat.simulate_traffic(internal_ip1, internal_port1, "93.184.216.34")  # Example external destination
nat.simulate_traffic(internal_ip2, internal_port2, "93.184.216.34")

# Simulate response from external to internal
nat.simulate_response("203.0.113.1", internal_port1, "93.184.216.34")
nat.simulate_response("203.0.113.1", internal_port2, "93.184.216.34")
