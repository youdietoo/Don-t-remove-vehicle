import unrealsdk

from mods_base import build_mod, hook
from unrealsdk.hooks import Type


@hook("WillowGame.Behavior_CheckMapChangeConditions:GetDestinationStationDefinition", Type.POST)
def get_destination_station_definition(obj, args, ret, caller):
    try:
        if ret is None:
            return

        old_value = ret.bAllowVehiclesToThisStation

        if old_value is False:
            ret.bAllowVehiclesToThisStation = True

    except Exception as e:
        print(f"[VehicleMapTransfer] ERROR: {e}")


build_mod()