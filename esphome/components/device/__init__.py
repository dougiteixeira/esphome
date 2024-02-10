import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import (
    CONF_ID,
    CONF_NAME,
    CONF_TYPE,
)

CODEOWNERS = ["@esphome/core"]
device_ns = cg.esphome_ns.namespace("device")
Device = device_ns.class_("Device", cg.Component)
MULTI_CONF = True

CONF_MANUFACTURER = "manufacturer"
ENTRY_TYPE_OPTIONS = {
    "SERVICE": "service",
}

CONFIG_SCHEMA = cv.Schema(
    {
        cv.Required(CONF_ID): cv.declare_id(Device),
        cv.Required(CONF_NAME): cv.string,
        cv.Optional(CONF_MANUFACTURER): cv.string,
        cv.Optional(CONF_TYPE): cv.enum(ENTRY_TYPE_OPTIONS, upper=True),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    cg.add(var.set_name(config[CONF_NAME]))
    cg.add(var.set_manufacturer(config[CONF_MANUFACTURER]))
    cg.add(var.set_entry_type(config[CONF_TYPE]))

    cg.add_define("USE_DEVICE")
