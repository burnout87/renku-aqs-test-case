#from astropy.coordinates import SkyCoord
import astroquery.desi

#astroquery.legacysurvey.LegacySurvey.query_object_async(SkyCoord(83,22, unit="deg"))

print(astroquery.desi.DESILegacySurvey.query_object)

r = astroquery.desi.DESILegacySurvey.query_object("ActualAstroObject")

print("astroquery returns:", r)

open("test-output.txt", "w").write("test!" + str(astroquery.hooked))

