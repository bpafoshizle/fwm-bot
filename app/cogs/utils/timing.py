import asyncio
from datetime import datetime, timedelta, timezone

import pytz

us_central_tz = pytz.timezone("US/Central")


async def wait_until(dt):
    """ Sleep until the specified datetime. Expects UTC """
    now = datetime.now(timezone.utc)
    await asyncio.sleep((dt - now).total_seconds())


def calc_tomorrow_6am():
    """ Calculate tomorrow 6am in US Central time. Convert to UTC. Return. """
    tmrw_6am_ct = datetime.now(us_central_tz) + timedelta(days=1)
    tmrw_6am_ct = tmrw_6am_ct.replace(hour=6, minute=0, second=0, microsecond=0)
    tmrw_6am_utc = tmrw_6am_ct.astimezone(timezone.utc)
    return tmrw_6am_utc
