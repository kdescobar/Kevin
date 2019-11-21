# Timing code for python3 (also works for python 2.7)

    ###################################
    # Timing function added by Kevin. This function allows the user specify the radio start time and resets the pps on the radio for syncronization. 
    # Code based on code from:
    # http://lists.ettus.com/pipermail/usrp-users_lists.ettus.com/attachments/20150115/66ac59c6/attachment-0002.html
    ####################################

    def timing(self):    
        
        # Get user time
        print('Type in desired start time (min only)')
        user_start_time = (int(input()),)

        # Convert local time to sturct_time format
        local_time = time.time()
        user_time = time.localtime(local_time)
        
        # Create future time in struct_time format
        t = user_time[0:4]+user_start_time+(0,)+user_time[6:9]
        
        # Convert future time to seconds
        future_time = time.mktime(t)

        # Set start time delay to time difference between future and local time
        start_time = int(future_time - local_time)
        
        # Set start time, where start_time > 2.0
        self.uhd_usrp_source_0.set_start_time(uhd.time_spec(start_time))
       
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
   
            print("last_pps0 : %6.12f"%uhd.time_spec_t.get_real_secs(last_pps0))
           
            time.sleep(1.0)
        
        # For completion varification
        print('Cute cuddly Kittens') 
        print(time.ctime())

