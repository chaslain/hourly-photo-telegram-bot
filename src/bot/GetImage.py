
import boto.s3
import time
import datetime
from os import getenv
from math import floor

class GetImage:

    def _get_image_number():
        beginning_timestamp = getenv("VERY_FIRST_PICTURE_TIMESTAMP")

        if beginning_timestamp == None:
            print("VERY_FIRST_PICTURE_TIMESTAMP not specified - no photo available.")
            return None
        
        dt: datetime.datetime = datetime.fromtimestamp(int(beginning_timestamp))

        now: datetime.datetime = datetime.gmtime()
        if beginning_timestamp > now:
            return None
        
        delta: datetime.timedelta = dt.get_item()

        return floor(delta.total_seconds / 3600)

    def get_image():
        number = GetImage._get_image_number()
        

        

        

        

