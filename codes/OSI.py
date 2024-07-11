class OSIModel:
    def __init__(self, data):
        self.data=data

    def application_layer(self):
        print("Application Layer: Processing data", self.data)
        self.data="application_processed("+self.data+")"
        self.presentation_layer()

    def presentation_layer(self):
        print("Presentation Layer: Formatting data", self.data)
        self.data="presentation_processed("+self.data+")"
        self.session_layer()

    def session_layer(self):
        print("Session Layer: Managing session for data", self.data)
        self.data="session_processed("+self.data+")"
        self.transport_layer()

    def transport_layer(self):
        print("Transport Layer: Segmenting data", self.data)
        self.data="transport_processed("+self.data+")"
        self.network_layer()

    def network_layer(self):
        print("Network Layer: Routing data", self.data)
        self.data="network_processed("+self.data+")"
        self.data_link_layer()

    def data_link_layer(self):
        print("Data Link Layer: Framing data", self.data)
        self.data="datalink_processed("+self.data+")"
        self.physical_layer()

    def physical_layer(self):
        print("Physical Layer: Transmitting data", self.data)
        self.data="physical_processed("+self.data+")"
        print("Final data transmitted:", self.data)

# Example usage
osi_model=OSIModel(data="Hello World")
osi_model.application_layer()
