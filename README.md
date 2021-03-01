# pythonRandLight
**randLight.py**<p>
  This script retreives a range of random numbers from a remote hardware RNG server via rest to control a set of Kasa smart plugs. This is meant to be used with [rngRestServer.py](https://github.com/deckerEnigmatic/rngRESTServer) as the remote server. This script was used as part of an [MMI experiment](https://www.enigmaticdevices.com/replicating-the-princeton-pear-lab-plant-rng-experiment/) involving the effects of random lighting on plant growth.<p> 
    [Python Kasa](https://github.com/python-kasa/python-kasa) library is a dependency. <p>
    **Parameters:** <p>
      low_range = lowest number in range <br/>
      high_range = highest number in range <br/>
      plant_position = location of plant<br/>
      plant_num = number of plants<br/>
      light_time = time in seconds for Kasa plug to remain 'on'<br/>
      log_handle = path to file <br/>
      sleep_factor = interval in seconds to wait before retreiving the next number </br>
      exper_num = numeric label for a specific run <p>
  
  Make sure to update the IP address of the remote RNG server before running.
      
      
