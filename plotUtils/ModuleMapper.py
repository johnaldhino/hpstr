#Module Mapper for 2019 layout
class ModuleMapper(dict):

    string_to_hw = {}
    string_to_sw = {}
    hw_to_string = {}
    hw_to_sw ={}
    sw_to_hw ={}
    sw_to_string = {}
    global_channel_map = {}
    def __init__(self):

        ModuleMapper.hw_to_sw["F0H0"] = "ly1_m0" ;
        ModuleMapper.hw_to_sw["F0H1"] = "ly2_m0" ;
        ModuleMapper.hw_to_sw["F0H2"] = "ly3_m0" ;
        ModuleMapper.hw_to_sw["F0H3"] = "ly4_m0" ;
        ModuleMapper.hw_to_sw["F1H0"] = "ly4_m1" ;
        ModuleMapper.hw_to_sw["F1H1"] = "ly3_m1" ;
        ModuleMapper.hw_to_sw["F1H2"] = "ly2_m1" ;
        ModuleMapper.hw_to_sw["F1H3"] = "ly1_m1" ;
        ModuleMapper.hw_to_sw["F2H0"] = "ly5_m0" ;
        ModuleMapper.hw_to_sw["F2H1"] = "ly6_m0" ;
        ModuleMapper.hw_to_sw["F2H2"] = "ly8_m0" ;
        ModuleMapper.hw_to_sw["F2H3"] = "ly7_m0" ;
        ModuleMapper.hw_to_sw["F3H0"] = "ly7_m1";
        ModuleMapper.hw_to_sw["F3H1"] = "ly8_m1";
        ModuleMapper.hw_to_sw["F3H2"] = "ly5_m1";
        ModuleMapper.hw_to_sw["F3H3"] = "ly6_m1";
        ModuleMapper.hw_to_sw["F4H0"] = "ly9_m0" ;
        ModuleMapper.hw_to_sw["F4H1"] = "ly9_m2" ;
        ModuleMapper.hw_to_sw["F4H2"] = "ly10_m0";
        ModuleMapper.hw_to_sw["F4H3"] = "ly10_m2";
        ModuleMapper.hw_to_sw["F5H0"] = "ly9_m1" ;
        ModuleMapper.hw_to_sw["F5H1"] = "ly9_m3" ;
        ModuleMapper.hw_to_sw["F5H2"] = "ly10_m1";
        ModuleMapper.hw_to_sw["F5H3"] = "ly10_m3";
        ModuleMapper.hw_to_sw["F6H0"] = "ly11_m0";
        ModuleMapper.hw_to_sw["F6H1"] = "ly11_m2";
        ModuleMapper.hw_to_sw["F6H2"] = "ly12_m0";
        ModuleMapper.hw_to_sw["F6H3"] = "ly12_m2";
        ModuleMapper.hw_to_sw["F7H0"] = "ly11_m1";
        ModuleMapper.hw_to_sw["F7H1"] = "ly11_m3";
        ModuleMapper.hw_to_sw["F7H2"] = "ly12_m1";
        ModuleMapper.hw_to_sw["F7H3"] = "ly12_m3";
        ModuleMapper.hw_to_sw["F8H0"] = "ly13_m0";
        ModuleMapper.hw_to_sw["F8H1"] = "ly13_m2";
        ModuleMapper.hw_to_sw["F8H2"] = "ly14_m0";
        ModuleMapper.hw_to_sw["F8H3"] = "ly14_m2";
        ModuleMapper.hw_to_sw["F9H0"] = "ly13_m1";
        ModuleMapper.hw_to_sw["F9H1"] = "ly13_m3";
        ModuleMapper.hw_to_sw["F9H2"] = "ly14_m1";
        ModuleMapper.hw_to_sw["F9H3"] = "ly14_m3";

        ModuleMapper.sw_to_hw["ly1_m0" ] = "F0H0" ;
        ModuleMapper.sw_to_hw["ly2_m0" ] = "F0H1" ;
        ModuleMapper.sw_to_hw["ly3_m0" ] = "F0H2" ;
        ModuleMapper.sw_to_hw["ly4_m0" ] = "F0H3" ;
        ModuleMapper.sw_to_hw["ly4_m1" ] = "F1H0" ;
        ModuleMapper.sw_to_hw["ly3_m1" ] = "F1H1" ;
        ModuleMapper.sw_to_hw["ly2_m1" ] = "F1H2" ;
        ModuleMapper.sw_to_hw["ly1_m1" ] = "F1H3" ;
        ModuleMapper.sw_to_hw["ly5_m0" ] = "F2H0" ;
        ModuleMapper.sw_to_hw["ly6_m0" ] = "F2H1" ;
        ModuleMapper.sw_to_hw["ly8_m0" ] = "F2H2" ;
        ModuleMapper.sw_to_hw["ly7_m0" ] = "F2H3" ;
        ModuleMapper.sw_to_hw["ly5_m1" ] = "F3H2" ;
        ModuleMapper.sw_to_hw["ly6_m1" ] = "F3H3" ;
        ModuleMapper.sw_to_hw["ly7_m1" ] = "F3H0" ;
        ModuleMapper.sw_to_hw["ly8_m1" ] = "F3H1" ;
        ModuleMapper.sw_to_hw["ly9_m0" ] = "F4H0" ;
        ModuleMapper.sw_to_hw["ly9_m2" ] = "F4H1" ;
        ModuleMapper.sw_to_hw["ly10_m0"] = "F4H2" ;
        ModuleMapper.sw_to_hw["ly10_m2"] = "F4H3" ;
        ModuleMapper.sw_to_hw["ly9_m1" ] = "F5H0" ;
        ModuleMapper.sw_to_hw["ly9_m3" ] = "F5H1" ;
        ModuleMapper.sw_to_hw["ly10_m1"] = "F5H2" ;
        ModuleMapper.sw_to_hw["ly10_m3"] = "F5H3" ;
        ModuleMapper.sw_to_hw["ly11_m0"] = "F6H0" ;
        ModuleMapper.sw_to_hw["ly11_m2"] = "F6H1" ;
        ModuleMapper.sw_to_hw["ly12_m0"] = "F6H2" ;
        ModuleMapper.sw_to_hw["ly12_m2"] = "F6H3" ;
        ModuleMapper.sw_to_hw["ly11_m1"] = "F7H0" ;
        ModuleMapper.sw_to_hw["ly11_m3"] = "F7H1" ;
        ModuleMapper.sw_to_hw["ly12_m1"] = "F7H2" ;
        ModuleMapper.sw_to_hw["ly12_m3"] = "F7H3" ;
        ModuleMapper.sw_to_hw["ly13_m0"] = "F8H0" ;
        ModuleMapper.sw_to_hw["ly13_m2"] = "F8H1" ;
        ModuleMapper.sw_to_hw["ly14_m0"] = "F8H2" ;
        ModuleMapper.sw_to_hw["ly14_m2"] = "F8H3" ;
        ModuleMapper.sw_to_hw["ly13_m1"] = "F9H0" ;
        ModuleMapper.sw_to_hw["ly13_m3"] = "F9H1" ;
        ModuleMapper.sw_to_hw["ly14_m1"] = "F9H2" ;
        ModuleMapper.sw_to_hw["ly14_m3"] = "F9H3" ;

        #HW to string and viceversa

        ModuleMapper.hw_to_string["F0H0"] = "L0T_axial"     ;
        ModuleMapper.hw_to_string["F0H1"] = "L0T_stereo"    ;
        ModuleMapper.hw_to_string["F0H2"] = "L1T_axial"     ;
        ModuleMapper.hw_to_string["F0H3"] = "L1T_stereo"    ;
        ModuleMapper.hw_to_string["F1H0"] = "L1B_axial"     ;
        ModuleMapper.hw_to_string["F1H1"] = "L1B_stereo"    ;
        ModuleMapper.hw_to_string["F1H2"] = "L0B_axial"     ;
        ModuleMapper.hw_to_string["F1H3"] = "L0B_stereo"    ;
        ModuleMapper.hw_to_string["F2H0"] = "L2T_axial"     ;
        ModuleMapper.hw_to_string["F2H1"] = "L2T_stereo"    ;
        ModuleMapper.hw_to_string["F2H2"] = "L3T_stereo"    ;
        ModuleMapper.hw_to_string["F2H3"] = "L3T_axial"     ;
        ModuleMapper.hw_to_string["F3H2"] = "L2B_stereo"    ;
        ModuleMapper.hw_to_string["F3H3"] = "L2B_axial"     ;
        ModuleMapper.hw_to_string["F3H0"] = "L3B_stereo"    ;
        ModuleMapper.hw_to_string["F3H1"] = "L3B_axial"     ;
        ModuleMapper.hw_to_string["F4H0"] = "L4T_axial_ele" ;
        ModuleMapper.hw_to_string["F4H1"] = "L4T_axial_pos" ;
        ModuleMapper.hw_to_string["F4H2"] = "L4T_stereo_ele";
        ModuleMapper.hw_to_string["F4H3"] = "L4T_stereo_pos";
        ModuleMapper.hw_to_string["F5H0"] = "L4B_stereo_ele";
        ModuleMapper.hw_to_string["F5H1"] = "L4B_stereo_pos";
        ModuleMapper.hw_to_string["F5H2"] = "L4B_axial_ele" ;
        ModuleMapper.hw_to_string["F5H3"] = "L4B_axial_pos" ;
        ModuleMapper.hw_to_string["F6H0"] = "L5T_axial_ele" ;
        ModuleMapper.hw_to_string["F6H1"] = "L5T_axial_pos" ;
        ModuleMapper.hw_to_string["F6H2"] = "L5T_stereo_ele";
        ModuleMapper.hw_to_string["F6H3"] = "L5T_stereo_pos";
        ModuleMapper.hw_to_string["F7H0"] = "L5B_stereo_ele";
        ModuleMapper.hw_to_string["F7H1"] = "L5B_stereo_pos";
        ModuleMapper.hw_to_string["F7H2"] = "L5B_axial_ele" ;
        ModuleMapper.hw_to_string["F7H3"] = "L5B_axial_pos" ;
        ModuleMapper.hw_to_string["F8H0"] = "L6T_axial_ele" ;
        ModuleMapper.hw_to_string["F8H1"] = "L6T_axial_pos" ;
        ModuleMapper.hw_to_string["F8H2"] = "L6T_stereo_ele";
        ModuleMapper.hw_to_string["F8H3"] = "L6T_stereo_pos";
        ModuleMapper.hw_to_string["F9H0"] = "L6B_stereo_ele";
        ModuleMapper.hw_to_string["F9H1"] = "L6B_stereo_pos";
        ModuleMapper.hw_to_string["F9H2"] = "L6B_axial_ele" ;
        ModuleMapper.hw_to_string["F9H3"] = "L6B_axial_pos" ; 

        ModuleMapper.string_to_hw["L0T_axial"     ] = "F0H0";
        ModuleMapper.string_to_hw["L0T_stereo"    ] = "F0H1";
        ModuleMapper.string_to_hw["L1T_axial"     ] = "F0H2";
        ModuleMapper.string_to_hw["L1T_stereo"    ] = "F0H3";
        ModuleMapper.string_to_hw["L1B_axial"     ] = "F1H0";
        ModuleMapper.string_to_hw["L1B_stereo"    ] = "F1H1";
        ModuleMapper.string_to_hw["L0B_axial"     ] = "F1H2";
        ModuleMapper.string_to_hw["L0B_stereo"    ] = "F1H3";
        ModuleMapper.string_to_hw["L2T_axial"     ] = "F2H0";
        ModuleMapper.string_to_hw["L2T_stereo"    ] = "F2H1";
        ModuleMapper.string_to_hw["L3T_stereo"    ] = "F2H2";
        ModuleMapper.string_to_hw["L3T_axial"     ] = "F2H3";
        ModuleMapper.string_to_hw["L2B_stereo"    ] = "F3H2";
        ModuleMapper.string_to_hw["L2B_axial"     ] = "F3H3";
        ModuleMapper.string_to_hw["L3B_stereo"    ] = "F3H0";
        ModuleMapper.string_to_hw["L3B_axial"     ] = "F3H1";
        ModuleMapper.string_to_hw["L4T_axial_ele" ] = "F4H0";
        ModuleMapper.string_to_hw["L4T_axial_pos" ] = "F4H1";
        ModuleMapper.string_to_hw["L4T_stereo_ele"] = "F4H2";
        ModuleMapper.string_to_hw["L4T_stereo_pos"] = "F4H3";
        ModuleMapper.string_to_hw["L4B_stereo_ele"] = "F5H0";
        ModuleMapper.string_to_hw["L4B_stereo_pos"] = "F5H1";
        ModuleMapper.string_to_hw["L4B_axial_ele" ] = "F5H2";
        ModuleMapper.string_to_hw["L4B_axial_pos" ] = "F5H3";
        ModuleMapper.string_to_hw["L5T_axial_ele" ] = "F6H0";
        ModuleMapper.string_to_hw["L5T_axial_pos" ] = "F6H1";
        ModuleMapper.string_to_hw["L5T_stereo_ele"] = "F6H2";
        ModuleMapper.string_to_hw["L5T_stereo_pos"] = "F6H3";
        ModuleMapper.string_to_hw["L5B_stereo_ele"] = "F7H0";
        ModuleMapper.string_to_hw["L5B_stereo_pos"] = "F7H1";
        ModuleMapper.string_to_hw["L5B_axial_ele" ] = "F7H2";
        ModuleMapper.string_to_hw["L5B_axial_pos" ] = "F7H3";
        ModuleMapper.string_to_hw["L6T_axial_ele" ] = "F8H0";
        ModuleMapper.string_to_hw["L6T_axial_pos" ] = "F8H1";
        ModuleMapper.string_to_hw["L6T_stereo_ele"] = "F8H2";
        ModuleMapper.string_to_hw["L6T_stereo_pos"] = "F8H3";
        ModuleMapper.string_to_hw["L6B_stereo_ele"] = "F9H0";
        ModuleMapper.string_to_hw["L6B_stereo_pos"] = "F9H1";
        ModuleMapper.string_to_hw["L6B_axial_ele" ] = "F9H2";
        ModuleMapper.string_to_hw["L6B_axial_pos" ] = "F9H3";


        #sw to string


        ModuleMapper.sw_to_string["ly1_m0" ] = "L0T_axial"     ;
        ModuleMapper.sw_to_string["ly2_m0" ] = "L0T_stereo"    ;
        ModuleMapper.sw_to_string["ly3_m0" ] = "L1T_axial"     ;
        ModuleMapper.sw_to_string["ly4_m0" ] = "L1T_stereo"    ;
        ModuleMapper.sw_to_string["ly4_m1" ] = "L1B_axial"     ;
        ModuleMapper.sw_to_string["ly3_m1" ] = "L1B_stereo"    ;
        ModuleMapper.sw_to_string["ly2_m1" ] = "L0B_axial"     ;
        ModuleMapper.sw_to_string["ly1_m1" ] = "L0B_stereo"    ;
        ModuleMapper.sw_to_string["ly5_m0" ] = "L2T_axial"     ;
        ModuleMapper.sw_to_string["ly6_m0" ] = "L2T_stereo"    ;
        ModuleMapper.sw_to_string["ly8_m0" ] = "L3T_stereo"    ;
        ModuleMapper.sw_to_string["ly7_m0" ] = "L3T_axial"     ;
        ModuleMapper.sw_to_string["ly5_m1" ] = "L2B_stereo"    ;
        ModuleMapper.sw_to_string["ly6_m1" ] = "L2B_axial"     ;
        ModuleMapper.sw_to_string["ly7_m1" ] = "L3B_stereo"    ;
        ModuleMapper.sw_to_string["ly8_m1" ] = "L3B_axial"     ;
        ModuleMapper.sw_to_string["ly9_m0" ] = "L4T_axial_ele" ;
        ModuleMapper.sw_to_string["ly9_m2" ] = "L4T_axial_pos" ;
        ModuleMapper.sw_to_string["ly10_m0"] = "L4T_stereo_ele";
        ModuleMapper.sw_to_string["ly10_m2"] = "L4T_stereo_pos";
        ModuleMapper.sw_to_string["ly9_m1" ] = "L4B_stereo_ele";
        ModuleMapper.sw_to_string["ly9_m3" ] = "L4B_stereo_pos";
        ModuleMapper.sw_to_string["ly10_m1"] = "L4B_axial_ele" ;
        ModuleMapper.sw_to_string["ly10_m3"] = "L4B_axial_pos" ;
        ModuleMapper.sw_to_string["ly11_m0"] = "L5T_axial_ele" ;
        ModuleMapper.sw_to_string["ly11_m2"] = "L5T_axial_pos" ;
        ModuleMapper.sw_to_string["ly12_m0"] = "L5T_stereo_ele";
        ModuleMapper.sw_to_string["ly12_m2"] = "L5T_stereo_pos";
        ModuleMapper.sw_to_string["ly11_m1"] = "L5B_stereo_ele";
        ModuleMapper.sw_to_string["ly11_m3"] = "L5B_stereo_pos";
        ModuleMapper.sw_to_string["ly12_m1"] = "L5B_axial_ele" ;
        ModuleMapper.sw_to_string["ly12_m3"] = "L5B_axial_pos" ;
        ModuleMapper.sw_to_string["ly13_m0"] = "L6T_axial_ele" ;
        ModuleMapper.sw_to_string["ly13_m2"] = "L6T_axial_pos" ;
        ModuleMapper.sw_to_string["ly14_m0"] = "L6T_stereo_ele";
        ModuleMapper.sw_to_string["ly14_m2"] = "L6T_stereo_pos";
        ModuleMapper.sw_to_string["ly13_m1"] = "L6B_stereo_ele";
        ModuleMapper.sw_to_string["ly13_m3"] = "L6B_stereo_pos";
        ModuleMapper.sw_to_string["ly14_m1"] = "L6B_axial_ele" ;
        ModuleMapper.sw_to_string["ly14_m3"] = "L6B_axial_pos" ;


        ModuleMapper.string_to_sw["L0T_axial"     ] = "ly1_m0" ;
        ModuleMapper.string_to_sw["L0T_stereo"    ] = "ly2_m0" ;
        ModuleMapper.string_to_sw["L1T_axial"     ] = "ly3_m0" ;
        ModuleMapper.string_to_sw["L1T_stereo"    ] = "ly4_m0" ;
        ModuleMapper.string_to_sw["L1B_axial"     ] = "ly4_m1" ;
        ModuleMapper.string_to_sw["L1B_stereo"    ] = "ly3_m1" ;
        ModuleMapper.string_to_sw["L0B_axial"     ] = "ly2_m1" ;
        ModuleMapper.string_to_sw["L0B_stereo"    ] = "ly1_m1" ;
        ModuleMapper.string_to_sw["L2T_axial"     ] = "ly5_m0" ;
        ModuleMapper.string_to_sw["L2T_stereo"    ] = "ly6_m0" ;
        ModuleMapper.string_to_sw["L3T_stereo"    ] = "ly8_m0" ;
        ModuleMapper.string_to_sw["L3T_axial"     ] = "ly7_m0" ;
        ModuleMapper.string_to_sw["L2B_stereo"    ] = "ly5_m1" ;
        ModuleMapper.string_to_sw["L2B_axial"     ] = "ly6_m1" ;
        ModuleMapper.string_to_sw["L3B_stereo"    ] = "ly7_m1" ;
        ModuleMapper.string_to_sw["L3B_axial"     ] = "ly8_m1" ;
        ModuleMapper.string_to_sw["L4T_axial_ele" ] = "ly9_m0" ;
        ModuleMapper.string_to_sw["L4T_axial_pos" ] = "ly9_m2" ;
        ModuleMapper.string_to_sw["L4T_stereo_ele"] = "ly10_m0";
        ModuleMapper.string_to_sw["L4T_stereo_pos"] = "ly10_m2";
        ModuleMapper.string_to_sw["L4B_stereo_ele"] = "ly9_m1" ;
        ModuleMapper.string_to_sw["L4B_stereo_pos"] = "ly9_m3" ;
        ModuleMapper.string_to_sw["L4B_axial_ele" ] = "ly10_m1";
        ModuleMapper.string_to_sw["L4B_axial_pos" ] = "ly10_m3";
        ModuleMapper.string_to_sw["L5T_axial_ele" ] = "ly11_m0";
        ModuleMapper.string_to_sw["L5T_axial_pos" ] = "ly11_m2";
        ModuleMapper.string_to_sw["L5T_stereo_ele"] = "ly12_m0";
        ModuleMapper.string_to_sw["L5T_stereo_pos"] = "ly12_m2";
        ModuleMapper.string_to_sw["L5B_stereo_ele"] = "ly11_m1";
        ModuleMapper.string_to_sw["L5B_stereo_pos"] = "ly11_m3";
        ModuleMapper.string_to_sw["L5B_axial_ele" ] = "ly12_m1";
        ModuleMapper.string_to_sw["L5B_axial_pos" ] = "ly12_m3";
        ModuleMapper.string_to_sw["L6T_axial_ele" ] = "ly13_m0";
        ModuleMapper.string_to_sw["L6T_axial_pos" ] = "ly13_m2";
        ModuleMapper.string_to_sw["L6T_stereo_ele"] = "ly14_m0";
        ModuleMapper.string_to_sw["L6T_stereo_pos"] = "ly14_m2";
        ModuleMapper.string_to_sw["L6B_stereo_ele"] = "ly13_m1";
        ModuleMapper.string_to_sw["L6B_stereo_pos"] = "ly13_m3";
        ModuleMapper.string_to_sw["L6B_axial_ele" ] = "ly14_m1";
        ModuleMapper.string_to_sw["L6B_axial_pos" ] = "ly14_m3";

        #For 2019 and 2021 only
        #Build svt global id map
        channel_index = 0
        for feb in range(10):
            str_feb = "F" + str(feb)
            max_channel = 640
            if feb < 2:
                max_channel = 512
            for hybrid in range(4):
                local_to_svtid_map = {}
                str_hybrid = "H" + str(hybrid)
                #print(str_feb + str_hybrid)
                for channel in range(max_channel):
                    svtid = channel_index + channel
                    local_to_svtid_map[channel] = svtid
                ModuleMapper.global_channel_map[str_feb + str_hybrid] = local_to_svtid_map
                channel_index = channel_index + max_channel
        [print(key,':', value) for key,value in ModuleMapper.global_channel_map.items()]


    def get_hw_to_string(self,string):
        return ModuleMapper.hw_to_string[string]

    def get_string_to_sw(self,string):
        return ModuleMapper.string_to_sw[string]

    def get_string_to_hw(self,string):
        return ModuleMapper.string_to_hw[string]

    def getSvtIDFromHWChannel(self,channel, hwTag):
        channelMap = ModuleMapper.global_channel_map[hwTag]
        try:
            svtid = channelMap[channel]
            return svtid
        except:
            print("Channel %s on %s does not exist. Failed to return global svtid")
            return null


