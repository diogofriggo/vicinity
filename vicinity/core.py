from functools import lru_cache

import numpy as np
import pandas as pd


EARTH_DIAMETER_KM = 12742.0
PI_OVER_180 = np.pi / 180.0
LAT_COL = 'NumCoordNEmpreendimento'
LON_COL = 'NumCoordEEmpreendimento'


@lru_cache(maxsize=None)
def read_cached_csv(file_path):
    df = pd.read_csv(file_path, sep=';', encoding='utf_16_le')
    df['dst_lat_degrees'] = df[LAT_COL].str.replace(',', '.').astype(float)
    df['dst_lon_degrees'] = df[LON_COL].str.replace(',', '.').astype(float)
    df['dst_lat_radians'] = df['dst_lat_degrees'] * PI_OVER_180
    df['dst_lon_radians'] = df['dst_lon_degrees'] * PI_OVER_180
    return df.drop(columns=[LAT_COL, LON_COL])


def compute_vicinity(df, src_lat_degrees, src_lon_degrees, radius_km):
    src_lat_radians = src_lat_degrees * PI_OVER_180
    src_lon_radians = src_lon_degrees * PI_OVER_180

    compute_distance_km_inplace(df, src_lat_radians, src_lon_radians)
    df = df[df['distance_km'] <= radius_km].copy()

    compute_bearing_degrees_inplace(df, src_lat_radians, src_lon_radians)

    return df.sort_values('distance_km')


def compute_distance_km_inplace(df, src_lat_radians, src_lon_radians):
    delta_lat_radians = 'dst_lat_radians - @src_lat_radians'
    delta_lon_radians = 'dst_lon_radians - @src_lon_radians'
    intermediate = f'0.5 - cos({delta_lat_radians}) / 2.0 + (1.0 - cos({delta_lon_radians})) / 2.0 * cos(dst_lat_radians) * cos(@src_lat_radians)'
    expression = f'distance_km = @EARTH_DIAMETER_KM * arcsin(sqrt({intermediate}))'
    df.eval(expression, inplace=True)


def compute_bearing_degrees_inplace(df, src_lat_radians, src_lon_radians):
    delta_lon_radians = 'dst_lon_radians - @src_lon_radians'
    x = f'cos(dst_lat_radians) * sin({delta_lon_radians})'
    y = f'cos(@src_lat_radians) * sin(dst_lat_radians) - sin(@src_lat_radians) * cos(dst_lat_radians) * cos({delta_lon_radians})'
    expression = f'bearing_radians = arctan2({x}, {y})'
    df.eval(expression, inplace=True)
    df['bearing_degrees'] = (df['bearing_radians'] / PI_OVER_180).apply(positive_bearing_degrees)


def positive_bearing_degrees(bearing_degrees):
    if bearing_degrees < 0.0:
        return bearing_degrees + 180.0
    return bearing_degrees
