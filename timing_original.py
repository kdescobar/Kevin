# Original code for timing based on python 2.7
#       This code will not work in python3!!!
# Kevin Escobar
# Last updated: 11/20/19

# Code based on code from:
# http://lists.ettus.com/pipermail/usrp-users_lists.ettus.com/attachments/20150115/66ac59c6/attachment-0002.html
    
    def timing(self):    
        
        # Get user time
        print('Type in desired start time (min only)')
        user_start_time = int(raw_input())

        # Convert user time to Seconds
        local_time = time.time()
        user_time = time.localtime(local_time)

        t = [0]*9
        for i in range(9):
            t[i] = user_time[i]

        t[4] = user_start_time
        t[5] = 0

        delay_time = time.mktime(t)
        start_time = int(delay_time - local_time)
        
        print('Waiting to start...')

        # Set start time, where start_time > 2.0
        self.uhd_usrp_source_0.set_start_time(uhd.time_spec(start_time))
       
       # Delay start time

        # Set to one radio next pps, initially
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec(0.0))
        curr_hw_time = self.uhd_usrp_source_0.get_time_last_pps()
        while curr_hw_time==self.uhd_usrp_source_0.get_time_last_pps():
            pass
        # Sleep for 50ms
        time.sleep(0.05)

        # Synchronize both radios time registers
        self.uhd_usrp_source_0.set_time_next_pps(uhd.time_spec_t(0.0))
   
        # Sleep for a couple seconds to make sure all usrp time registers latched and settled
        time.sleep(2)
   
   
        # Check the last pps time
        for ii in range(0,5):
            last_pps0 = self.uhd_usrp_source_0.get_time_last_pps()
   
            print "last_pps0 : %6.12f"%uhd.time_spec_t.get_real_secs(last_pps0)
           
            time.sleep(1.0)
             
        print('Cute cuddly Kittens') 
        print(time.ctime())
