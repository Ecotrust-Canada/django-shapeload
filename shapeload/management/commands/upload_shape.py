from django.core.management.base import BaseCommand, CommandError
import os
from django.contrib.gis.gdal import DataSource
from vessel.models import SubArea
from django.contrib.gis.utils import LayerMapping

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        shapefile = args[0]
        ds = DataSource(shapefile)
        lyr = ds[0]
        print('length:',len(lyr))
        print('geom type:',str(lyr.geom_type))
        srs = lyr.srs
        print('srs:',str(srs))
        print('fields:',lyr.fields)
        for feat in lyr:
            print lyr.fields[0], ':', feat.get(lyr.fields[0]), feat.geom.num_points

        lm = LayerMapping(SubArea, shapefile, {'name':'Softshell','geom':'POLYGON'})
        lm.save()
        self.stdout.write('Successfully uploaded shape "%s"' % 99)
