# coding: utf-8

import unittest
from pyqweather import QWeatherConfig
from pyqweather.factories import QWeatherFactory

from pyqweather.auth import EnvironmentVariableSimpleAuthCredential

class TestMethods(unittest.TestCase):
    
    
  def test_qweather_geo_city_lookup(self):
    
    conf = QWeatherConfig(EnvironmentVariableSimpleAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_geo_pack(conf)
    
    self.assertTrue(pack is not None)
    
    resp = pack.city_lookup('北京')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(len(resp.location) > 0)

    
    
  def test_qweather_geo_city_top(self):
    
    conf = QWeatherConfig(EnvironmentVariableSimpleAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_geo_pack(conf)
    
    self.assertTrue(pack is not None)
    
    resp = pack.city_top()
    self.assertEqual('200', resp.get_code())  
        
    self.assertTrue(len(resp.top_city_list) > 0)
    
    
  def test_qweather_geo_poi_lookup(self):
    
    conf = QWeatherConfig(EnvironmentVariableSimpleAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_geo_pack(conf)
    
    self.assertTrue(pack is not None)
    
    resp = pack.poi_lookup('北京', 'scenic')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(len(resp.poi) > 0)    
    
  def test_qweather_geo_poi_range(self):
    
    conf = QWeatherConfig(EnvironmentVariableSimpleAuthCredential())
    factory = QWeatherFactory()
    pack = factory.create_geo_pack(conf)
    
    self.assertTrue(pack is not None)
    
    resp = pack.poi_range('116.41,39.92', 'scenic')
    self.assertEqual('200', resp.get_code())
    
    self.assertTrue(len(resp.poi) > 0)      

    
    

if __name__ == '__main__':
  
  unittest.main(verbosity=2)
  