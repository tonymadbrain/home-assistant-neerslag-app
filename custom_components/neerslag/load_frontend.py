from homeassistant.core import HomeAssistant
from homeassistant.components.frontend import add_extra_js_url
from homeassistant.components.http import StaticPathConfig
import logging
from .const import FRONTEND_SCRIPT_URL

_LOGGER = logging.getLogger(__name__)


async def setup_view(hass: HomeAssistant):
    """Register frontend card."""

    await hass.http.async_register_static_paths(
        [
            StaticPathConfig(
                FRONTEND_SCRIPT_URL,
                hass.config.path("custom_components/neerslag/home-assistant-neerslag-card/neerslag-card.js"),
                cache_headers=False,
            )
        ]
    )

    # Register as ES module
    add_extra_js_url(hass, FRONTEND_SCRIPT_URL , es5=False)

    _LOGGER.debug("Neerslag frontend registered")
