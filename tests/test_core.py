import numpy as np
import pandas as pd

from vicinity import core

def test_compute_distance_km_inplace():
    src_lat = -20.12479858 * core.PI_OVER_180
    src_lon = -43.8702025 * core.PI_OVER_180
    df = pd.DataFrame({
        'dst_lat_radians': [-20.18734167 * core.PI_OVER_180],
        'dst_lon_radians': [-43.8117525 * core.PI_OVER_180],
    })

    core.compute_distance_km_inplace(df, src_lat, src_lon)
    actual = df['distance_km'].iloc[0]

    # expected value has been computed from the following website using the pairs of coordinates above
    # https://www.meridianoutpost.com/resources/etools/calculators/calculator-latitude-longitude-distance.php?
    expected = 9.25
    np.testing.assert_almost_equal(actual, expected, decimal=2)



def test_compute_bearing_degrees_inplace():
    src_lat_degrees = -20.12479858 * core.PI_OVER_180
    src_lon_degrees = -43.8702025 * core.PI_OVER_180
    df = pd.DataFrame({
        'dst_lat_radians': [-20.18734167 * core.PI_OVER_180],
        'dst_lon_radians': [-43.8117525 * core.PI_OVER_180],
    })

    core.compute_bearing_degrees_inplace(df, src_lat_degrees, src_lon_degrees)
    actual = df['bearing_degrees'].iloc[0]

    # expected value has been computed from the following website using the pairs of coordinates above
    # http://instantglobe.com/CRANES/GeoCoordTool.html
    expected = 138.74890495432749
    np.testing.assert_almost_equal(actual, expected, decimal=2)