class BatteryCC: 
    def __init__(self, battery: Battery, initial_soc: float) -> NONE: ...
    def step(self, i_in: float, dt: float, measured_v=None) -> NONE: ...
    def soc(self) -> array: ...